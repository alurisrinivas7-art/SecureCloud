from fastapi import FastAPI, HTTPException
import psycopg
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


class Item(BaseModel):
    name: str
    description: Optional[str] = None


def check_database_connection():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            return cursor.fetchone()[0] == 1


def create_item(item: Item):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO items (name, description)
                VALUES (%s, %s)
                RETURNING id, name, description
                """,
                (item.name, item.description),
            )
            row = cursor.fetchone()
            conn.commit()

    return {
        "id": row[0],
        "name": row[1],
        "description": row[2],
    }

def get_items():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, name, description
                FROM items
                ORDER BY id
                """
            )
            rows = cursor.fetchall()

    return [
        {
            "id": row[0],
            "name": row[1],
            "description": row[2],
        }
        for row in rows
    ]
def update_item(item_id: int, item: Item):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE items
                SET name = %s, description = %s
                WHERE id = %s
                RETURNING id, name, description
                """,
                (item.name, item.description, item_id),
            )
            row = cursor.fetchone()
            conn.commit()

    if row is None:
        return None

    return {
        "id": row[0],
        "name": row[1],
        "description": row[2],
    }
def delete_item(item_id: int):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM items
                WHERE id = %s
                RETURNING id, name, description
                """,
                (item_id,),
            )
            row = cursor.fetchone()
            conn.commit()

    if row is None:
        return None

    return {
        "id": row[0],
        "name": row[1],
        "description": row[2],
    }
app = FastAPI(
    title="SecureCloud API",
    description="A secure cloud application for DevSecOps learning",
    version="1.0.0",
)
@app.post("/items")
def add_item(item: Item):
    return create_item(item)

@app.get("/")
def root():
    return {
        "message": "Welcome to SecureCloud API",
        "status": "running",
    }

@app.get("/items")
def list_items():
    return get_items()

@app.put("/items/{item_id}")
def edit_item(item_id: int, item: Item):
    result = update_item(item_id, item)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Item {item_id} not found",
        )

    return result

@app.delete("/items/{item_id}")
def remove_item(item_id: int):
    result = delete_item(item_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Item {item_id} not found",
        )

    return result

@app.get("/health")
def health_check():
    database_ok = check_database_connection()

    return {
        "status": "healthy",
        "database": "connected" if database_ok else "disconnected",
    }