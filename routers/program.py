from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models.program import Program, ProgramUpdate

router = APIRouter()

@router.get("/", tags=["program"], response_description="List all program", response_model=List[Program])
def list_program(request: Request):
    programs = list(request.app.database["program"].find(limit=100))
    return programs

@router.post("/", tags=["program"], response_description="Create a new program", status_code=status.HTTP_201_CREATED, response_model=Program)
def create_program(request: Request, program: Program = Body(...)):
    program = jsonable_encoder(program)
    new_program = request.app.database["program"].insert_one(program)
    created_program = request.app.database["program"].find_one(
        {"_id": new_program.inserted_id}

    )

    return created_program

@router.get("/{id}", response_description="Get a single program by id", response_model=Program)
def find_program(id: str, request: Request):
    if (program := request.app.database["program"].find_one({"_id": id})) is not None:
        return program
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Program with ID {id} not found")

@router.put("/{id}", response_description="Update a program", response_model=Program)
def update_program(id: str, request: Request, program: ProgramUpdate = Body(...)):
    program = {k: v for k, v in program.dict().items() if v is not None}
    if len(programk) >= 1:
        update_result = request.app.database["program"].update_one(
            {"_id": id}, {"$set": program}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Program with ID {id} not found")

    if (
        existing_program := request.app.database["program"].find_one({"_id": id})
    ) is not None:
        return existing_program

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Program with ID {id} not found")

@router.delete("/{id}", response_description="Delete a program")
def delete_program(id: str, request: Request, response: Response):
    delete_result = request.app.database["program"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Program with ID {id} not found")