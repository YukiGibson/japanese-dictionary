from typing import Optional

from fastapi import FastAPI

bengaku = FastAPI()


@bengaku.get("/")
def read_root():
    return {"Hello": "World"}


@bengaku.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}