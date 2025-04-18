import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Reps(BaseModel):
    id: int
    min: str = Field(...)
    max: str = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": 1,
                "min": "2",
                "max": "6"
                }
        }

class RepsUpdate(BaseModel):
    min: Optional[str]
    max: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "min": "2",
                "max": "6"
            }
        }