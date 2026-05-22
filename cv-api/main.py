# pyrefly: ignore [missing-import]
from contextlib import asynccontextmanager

from fastapi import FastAPI
# pyrefly: ignore [missing-import]
from ultralytics import YOLO

# 1. Define the lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load YOLOv8 model at startup and save in app state
    app.state.model = YOLO("yolov8n.pt")
    yield
    print("Shutting down the Computer Vision API service...")

# 2. Create the FastAPI instance
app = FastAPI(
    title="Computer Vision API",
    lifespan=lifespan
)

# 3. Create the basic health check route
@app.get("/")
async def health_check():
    return {"status": "ok"}
