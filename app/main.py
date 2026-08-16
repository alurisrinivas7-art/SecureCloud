from fastapi import FastAPI
import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI(
    title="SecureCloud API",
    description="A secure cloud application for DevSecOps learning",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to SecureCloud API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }