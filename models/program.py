import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Program(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    type: str = Field(...)
    musclegroup: str = Field(...)
    exercise: str = Field(...)
    sets: int = Field(...)
    minreprange: int = Field(...)
    maxregrange: int = Field(...)
    rest: int = Field(...)
    weight: int = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "novice",
                "experience": 12
                }
        }

class ProgramUpdate(BaseModel):
    name: Optional[str]
  

    class Config:
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "novice",
                "experience": 12
            }
        }