from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    rand = random.randint(1,10)
    txt = f"Випадковe число від 1 до 10: {rand}"
    return txt