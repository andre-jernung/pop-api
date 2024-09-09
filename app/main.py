from os import environ
import json
from typing import Optional, List, Dict, Union
from loguru import logger

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse

app = FastAPI(title="DSW POP API")

persons = json.loads(open("app/testdata.json").read())

@app.get("/search-person", response_model=Dict[str, List[Dict[str, str]]])
def search_person(query: str = Query(..., min_length=1)):
    results = []
    for key, value in persons.items():
        if query.lower() in value["name"].lower():
            results.append({"id": key, **value})
    if not results:
        raise HTTPException(status_code=404, detail="No persons found matching the query")
    return {"persons": results}
