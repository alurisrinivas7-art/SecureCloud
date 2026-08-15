from fastapi import FastAPI

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