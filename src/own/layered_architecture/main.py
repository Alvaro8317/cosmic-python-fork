from fastapi import FastAPI
from presentation.controller import router

app = FastAPI()
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
