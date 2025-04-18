from typing import Optional
from pydantic import BaseModel, Field
import uuid

class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    age: int = Field(...)
    weight: int = Field(...)
    height: int = Field(...)
    gender: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "ahmed",
                "age": 2,
                "weight": 10,
                "height": 12,
                "gender": "M"
                }
        }

class UserUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    height: Optional[int]
    weight: Optional[int]
    gender: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "ahmed",
                "age": 2,
                "weight": 10,
                "height": 12,
                "gender": "M"
            }
        }