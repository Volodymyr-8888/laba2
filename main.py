from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
async def root():
    rand = random.randint(1,6)
    txt = f"Випадковe число від 1 до 6: {rand}"
    return txt