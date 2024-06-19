import uvicorn
from fastapi import FastAPI

from app.routes import lcresponse
from config import settings

app = FastAPI()

app.include_router(lcresponse.router, prefix='/summarize')


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI!"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
