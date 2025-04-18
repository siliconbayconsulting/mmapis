from typing import Optional
from pydantic import BaseModel, Field
import uuid

class Lead(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    lastName: str = Field(...)
    firstName: str = Field(...)
    emailid: str = Field(...)
    contact: str = Field(...)
    age: int = Field(...)
    gender: str = Field(...)
    activityLevel: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "lastName": "ahmed",
                "firstName": "ahmed",
                "emailid": "ahmed",
                "contact": "ahmed",
                "age": 2,
                "gender": "M",
                "activityLevel": "sdfs"
                }
        }

class LeadUpdate(BaseModel):
    lastName: str = Field(...)
    firstName: str = Field(...)
    emailid: str = Field(...)
    contact: str = Field(...)
    age: int = Field(...)
    gender: str = Field(...)


    class Config:
        schema_extra = {
            "example": {
               "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "lastName": "ahmed",
                "firstName": "ahmed",
                "emailid": "ahmed",
                "contact": "ahmed",
                "age": 2,
                "gender": "M", "activityLevel": "sdfs"
            }
        }