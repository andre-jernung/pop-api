from os import environ
import json
from typing import Optional, List, Dict, Union
from loguru import logger

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse

app = FastAPI(title="DSW POP API")

persons = json.loads(open("app/testdata.json").read())

@app.get("/hello")
def say_hello():
    return {"hello": "hello world!"}

@app.get("/person/{person_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"person_id": item_id, "q": q}

@app.get("/search-person", response_model=Dict[str, List[Dict[str, str]]])
def search_person(query: str = Query(..., min_length=1)):
    results = []
    for key, value in persons.items():
        if query.lower() in value["name"].lower():
            results.append({"id": key, **value})
    if not results:
        raise HTTPException(status_code=404, detail="No persons found matching the query")
    return {"items": results}
