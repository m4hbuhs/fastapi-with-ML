from pydantic import BaseModel, Field
from typing import Dict


class PredictionResponse(BaseModel):
    prediction_category: str = Field(description="Predicted loan status" )
    confidence: float = Field( description="Model confidence score",ge=0,le=1)
    approved_probability: float = Field( description="Probability of loan approval", ge=0,le=1)
    rejected_probability: float = Field( description="Probability of loan rejection",ge=0,le=1)