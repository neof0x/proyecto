from fastapi import FastAPI
from routes.input import input_router



app= FastAPI()

app.include_router(input_router)

