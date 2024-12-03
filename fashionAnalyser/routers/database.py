from fastapi import FastAPI,HTTPException
from typing import Optional
from pydantic import BaseModel
from pymongo import MongoClient

# MongoDB connection details
MONGO_URI = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.2"
DATABASE_NAME = "fashion_Analysis"
#app=FastAPI()
# Dependency to get the database connection
#@app.get("/")
def getDB():
    try:
        client = MongoClient(MONGO_URI)
        db = client[DATABASE_NAME]
        # Test the connection by attempting to fetch server info
        client.server_info()  # This raises an exception if the connection is not successful
        # print(db)
        # print(db.list_collection_names())
        # print(list(db.userDetails.find()))
        return db
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {e}")
