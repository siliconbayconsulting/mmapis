from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models.rest import Rest, RestUpdate

router = APIRouter()

@router.get("/", tags=["rest"], response_description="List all rest", response_model=List[Rest])
def list_rest(request: Request):
    rest = list(request.app.database["rest"].find(limit=100))
    return rest

@router.post("/", tags=["rest"], response_description="Create a new rest", status_code=status.HTTP_201_CREATED, response_model=Rest)
def create_rest(request: Request, rest: Rest = Body(...)):
    rest = jsonable_encoder(rest)
    new_rest = request.app.database["rest"].insert_one(rest)
    created_rest = request.app.database["rest"].find_one(
        {"_id": new_rest.inserted_id}
    )

    return created_rest

@router.get("/{id}", response_description="Get a single rest by id", response_model=Rest)
def find_rest(id: str, request: Request):
    if (rest := request.app.database["rest"].find_one({"_id": id})) is not None:
        return rest
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Rest with ID {id} not found")

@router.put("/{id}", response_description="Update a rest", response_model=Rest)
def update_rest(id: str, request: Request, rest: RestUpdate = Body(...)):
    rest = {k: v for k, v in rest.dict().items() if v is not None}
    if len(restk) >= 1:
        update_result = request.app.database["rest"].update_one(
            {"_id": id}, {"$set": rest}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Rest with ID {id} not found")

    if (
        existing_rest := request.app.database["rest"].find_one({"_id": id})
    ) is not None:
        return existing_rest

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Rest with ID {id} not found")

@router.delete("/{id}", response_description="Delete a rest")
def delete_rest(id: str, request: Request, response: Response):
    delete_result = request.app.database["rest"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Rest with ID {id} not found")