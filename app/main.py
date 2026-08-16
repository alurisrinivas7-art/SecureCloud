from fastapi import FastAPI
import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def check_database_connection():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            return cursor.fetchone()[0] == 1
        
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
    database_ok = check_database_connection()

    return {
        "status": "healthy",
        "database": "connected" if database_ok else "disconnected",
    }