from pymongo import MongoClient
from app.config import settings


class MongoDB:
    """
    MongoDB connection handler.
    """

    def __init__(self):
        self.client = MongoClient(settings.MONGO_URI)
        self.db = self.client["vaultdb"]

        # Collections
        self.users = self.db["users"]
        self.vault = self.db["vault"]


mongodb = MongoDB()
