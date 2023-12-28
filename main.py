from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from src.generators import generate_annotation, generate_intro


app = FastAPI()


class TextIn(BaseModel):
    text: str


class TextOut(BaseModel):
    generation: str


@app.get("/generate_intro/", response_model=TextOut)
def generate_intro(text_in: TextIn):
    intro  = generate_intro(text_in)

    return {"generation": intro["generated_text"]}


@app.get("/generate_annotation/", response_model=TextOut)
def generate_intro(text_in: TextIn):
    annotation  = generate_annotation(text_in)

    return {"generation": annotation["generated_text"]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
