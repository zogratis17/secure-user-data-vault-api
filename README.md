# 🔐 Secure User Data Vault API

A production-style backend system for securely storing and retrieving
sensitive user data such as personal notes, API keys, and secrets.

Built with security, scalability, and real-world backend architecture in
mind.

------------------------------------------------------------------------

## 🚀 Features

-   User registration & login
-   Password hashing (bcrypt)
-   JWT authentication
-   AES encryption for stored data
-   Protected APIs
-   MongoDB Atlas integration
-   Input validation
-   Secure error handling
-   Environment-based configuration

------------------------------------------------------------------------

## 🧠 Architecture

Client → FastAPI → Security Layer → Database

Security Layers: - Authentication → JWT - Password Storage → bcrypt -
Data Storage → AES encryption

------------------------------------------------------------------------

## 🔑 Authentication Flow

1.  User registers
2.  Password is hashed before storage
3.  User logs in
4.  JWT token is issued
5.  Token required for protected routes

------------------------------------------------------------------------

## 🔐 Encryption Flow

1.  User sends sensitive data
2.  API encrypts data using AES (Fernet)
3.  Only encrypted data stored in DB
4.  Decrypted only when requested by authenticated user

------------------------------------------------------------------------

## 📦 Tech Stack

-   FastAPI
-   MongoDB Atlas
-   JWT (python-jose)
-   bcrypt (passlib)
-   AES encryption (cryptography)
-   Pydantic validation

------------------------------------------------------------------------

## ⚙️ Installation

Clone repo:

    git clone https://github.com/zogratis17/secure-user-data-vault-api.git
    cd secure-user-data-vault-api

Install dependencies:

    pip install -r requirements.txt

Create `.env`

    JWT_SECRET_KEY=your_secret
    FERNET_KEY=your_key
    MONGO_URI=your_mongo_uri

Run server:

    uvicorn app.main:app --reload

------------------------------------------------------------------------

## 📡 API Endpoints

### Auth

-   POST `/auth/register`
-   POST `/auth/login`

### Vault

-   POST `/vault/`
-   GET `/vault/`

------------------------------------------------------------------------

## 🛡 Security Measures Implemented

-   Password hashing
-   Token authentication
-   Encrypted storage
-   Input validation
-   Secure error responses
-   Environment secrets

------------------------------------------------------------------------

## 🧪 Testing

Interactive docs available at:

    /docs

------------------------------------------------------------------------

## 📈 Future Improvements

-   Refresh tokens
-   Role-based access
-   Rate limiting
-   Audit logs
-   Key rotation
