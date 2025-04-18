from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models.lead import Lead, LeadUpdate

router = APIRouter()

@router.get("/", tags=["lead"], response_description="List all leads", response_model=List[Lead])
def list_lead(request: Request):
    lead = list(request.app.database["lead"].find(limit=100))
    return lead

@router.post("/", tags=["lead"], response_description="Create a new lead", status_code=status.HTTP_201_CREATED, response_model=Lead)
def create_lead(request: Request, lead: Lead = Body(...)):
    lead = jsonable_encoder(lead)
    print(lead)    

    new_lead = request.app.database["lead"].insert_one(lead)
    created_lead = request.app.database["lead"].find_one(
        {"_id": new_lead.inserted_id}

    # Assign lead with a program
    # 1. Get Programs
    # 2. Select program
    # 3. Assign program
    # 4. return data
    )

    return created_lead

@router.get("/{id}", response_description="Get a single lead by id", response_model=Lead)
def find_lead(id: str, request: Request):
    if (lead := request.app.database["lead"].find_one({"_id": id})) is not None:
        return lead
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Lead with ID {id} not found")

@router.put("/{id}", response_description="Update a lead", response_model=Lead)
def update_lead(id: str, request: Request, lead: LeadUpdate = Body(...)):
    lead = {k: v for k, v in lead.dict().items() if v is not None}
    if len(lead) >= 1:
        update_result = request.app.database["lead"].update_one(
            {"_id": id}, {"$set": lead}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Lead with ID {id} not found")

    if (
        existing_lead := request.app.database["lead"].find_one({"_id": id})
    ) is not None:
        return existing_lead

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Lead with ID {id} not found")

@router.delete("/{id}", response_description="Delete a lead")
def delete_lead(id: str, request: Request, response: Response):
    delete_result = request.app.database["lead"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Lead with ID {id} not found")