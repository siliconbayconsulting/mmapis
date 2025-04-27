from typing import Optional
from pydantic import BaseModel, Field
import uuid

class Lead(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    email: str = Field(...)
    phoneNo: str = Field(...)
    age: int = Field(...)
    # gender: str = Field(...)
    enthusiastTrainer: bool = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "ahmed",
                "email": "ahmed",
                "phoneNo": "9346425221",
                "age": 2,
                "enthusiastTrainer": "false",
                }
        }

class LeadUpdate(BaseModel):
    name: str = Field(...)
    email: str = Field(...)
    phoneNo: str = Field(...)
    age: int = Field(...)
    # gender: str = Field(...)
    enthusiastTrainer: bool = Field(...)

    class Config:
        schema_extra = {
            "example": {
               "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "ahmed",
                "email": "ahmed",
                "phoneNo": "9346425221",
                "age": 2,
                "gender": "M",
                "enthusiastTrainer": "false",
            }
        }