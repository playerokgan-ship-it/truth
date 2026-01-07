from fastapi import FastAPI
import os
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/sum")
def sum_(a: int, b: int):
    return {"result": a + b}

