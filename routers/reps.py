from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models.reps import Reps, RepsUpdate

router = APIRouter()

@router.get("/", tags=["reps"], response_description="List all reps", response_model=List[Reps])
def list_reps(request: Request):
    reps = list(request.app.database["reps"].find(limit=100))
    return reps

@router.post("/", tags=["reps"], response_description="Create a new reps", status_code=status.HTTP_201_CREATED, response_model=Reps)
def create_reps(request: Request, reps: Reps = Body(...)):
    reps = jsonable_encoder(reps)
    new_reps = request.app.database["reps"].insert_one(reps)
    created_reps = request.app.database["reps"].find_one(
        {"_id": new_reps.inserted_id}
    )

    return created_reps

@router.get("/{id}", response_description="Get a single reps by id", response_model=Reps)
def find_reps(id: str, request: Request):
    if (reps := request.app.database["reps"].find_one({"_id": id})) is not None:
        return reps
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Reps with ID {id} not found")

@router.put("/{id}", response_description="Update a reps", response_model=Reps)
def update_reps(id: str, request: Request, reps: RepsUpdate = Body(...)):
    reps = {k: v for k, v in reps.dict().items() if v is not None}
    if len(repsk) >= 1:
        update_result = request.app.database["reps"].update_one(
            {"_id": id}, {"$set": reps}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Reps with ID {id} not found")

    if (
        existing_reps := request.app.database["reps"].find_one({"_id": id})
    ) is not None:
        return existing_reps

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Reps with ID {id} not found")

@router.delete("/{id}", response_description="Delete a reps")
def delete_reps(id: str, request: Request, response: Response):
    delete_result = request.app.database["reps"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Reps with ID {id} not found")