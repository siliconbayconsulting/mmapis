from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routers import program,book,reps,rest,user,lead
from fastapi.middleware.cors import CORSMiddleware

config = dotenv_values(".env")

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
     allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lead.router,tags=["lead"], prefix="/lead")
app.include_router(user.router,tags=["user"], prefix="/user")
app.include_router(program.router,tags=["program"], prefix="/program")
app.include_router(book.router,tags=["books"], prefix="/book")
app.include_router(reps.router,tags=["reps"], prefix="/reps")
app.include_router(rest.router,tags=["rest"], prefix="/rest")


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


@app.get("/")
def root():
    return {"Hello":"World"}


