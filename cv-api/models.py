# pyrefly: ignore [missing-import]
from pydantic import BaseModel

# The rectangle drawn around a detected object
# All values are pixel position (int)
class BoundingBox(BaseModel):
    xmin: int
    ymin: int
    xmax: int
    ymax: int

# One detected object in the image
# box = rectangle arount it
# label = what it is (e.g. "car", "person")
# confidence = how sure the model is (0.0 - 1.0)
class Prediction(BaseModel):
    box: BoundingBox
    label: str
    confidence: float

# Full response your API sends back
# status = "success" / "error"
# filename
# predictions =  list of everything detected in the image
class PredictionResponse(BaseModel):
    status: str
    filename: str
    predictions: list[Prediction]

