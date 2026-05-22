# cv-api — Computer Vision API
A FastAPI service that runs YOLOv8 object detection on uploaded images.

## What it does
- Accepts a POST request with an image file (jpg, jpeg, png, max 5MB)
- Validates file format and size before processing
- Runs YOLOv8 inference and returns bounding boxes, labels, and confidence scores
- Rejects invalid input with proper HTTP 400 errors

## Run locally

```bash
cd cv-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Test with curl

```bash
curl -X POST http://localhost:8000/api/v1/predict \
  -F "file=@your_image.jpg"
```

## Sample response

```json
{
  "status": "success",
  "filename": "your_image.jpg",
  "predictions": [
    {
      "box": { "xmin": 120, "ymin": 340, "xmax": 250, "ymax": 480 },
      "label": "car",
      "confidence": 0.945
    }
  ]
}
```

## Stack
- FastAPI + Uvicorn
- YOLOv8 (ultralytics)
- Pydantic v2
- Pillow

## Files
- `main.py` — FastAPI app, endpoint, validation, inference logic
- `models.py` — Pydantic response models
- `requirements.txt` — dependencies