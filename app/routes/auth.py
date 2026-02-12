from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserRegister, UserResponse
from app.models.user import UserModel
from app.database import mongodb
from app.core.security import hash_password
from app.schemas.user import UserLogin
from app.core.security import verify_password, create_access_token


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: UserRegister):
    """
    Register a new user.
    """

    # Check if user exists
    existing = mongodb.users.find_one({"email": user.email})
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # Hash password
    hashed = hash_password(user.password)

    # Create user model
    user_model = UserModel(
        email=user.email,
        hashed_password=hashed
    )

    # Insert into DB
    result = mongodb.users.insert_one(user_model.to_dict())

    return {
        "id": str(result.inserted_id),
        "email": user.email
    }

@router.post("/login")
def login(user: UserLogin):
    """
    Authenticate user and return JWT token.
    """

    # Find user
    db_user = mongodb.users.find_one({"email": user.email})

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Verify password
    if not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create token
    token = create_access_token({"sub": str(db_user["_id"])})

    return {"access_token": token, "token_type": "bearer"}
