# ml-engineering-exercises

Two hands-on ML Engineering projects built as part of an AI Engineer internship exercise.
Each project is self-contained with its own dependencies and README.

## Projects

### 1. `cv-api/` — Computer Vision API
A REST API that accepts an image and returns object detection results.
Built with FastAPI + YOLOv8. Callable from outside via curl or Postman.

### 2. `etl-pipeline/` — Multilingual ETL Pipeline
An automated pipeline that extracts text from YouTube or a news website,
cleans it, summarizes it, translates it into English and Vietnamese using an LLM,
then stores the result in a local database.

## Stack
- Python 3.12
- FastAPI, Uvicorn, Pydantic
- YOLOv8 (ultralytics)
- Gemini 2.5 Flash (google-genai)
- SQLite / MongoDB
- Pillow, OpenCV

## Status
- [ ] cv-api — in progress
- [ ] etl-pipeline — not started

## Author
An Loc Nguyen — Year 2 CS @ NTU Singapore
AI Engineering Intern