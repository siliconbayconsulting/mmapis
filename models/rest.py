from typing import Optional
from pydantic import BaseModel, Field

class Rest(BaseModel):
    id: int
    period: int = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": 1,
                "period": 30
                }
        }

class RestUpdate(BaseModel):
    period: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "period": 20
            }
        }