from os import environ
import json
from typing import Optional, List, Dict, Union
from loguru import logger

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse

app = FastAPI(title="DSW POP API")

persons = json.loads(open("app/testdata.json").read())
organisations = json.loads(open("app/orgdata.json").read())

@app.get("/search-person", response_model=Dict[str, List[Dict[str, str]]])
def search_person(query: str = Query(..., min_length=1)):
    results = []
    for key, value in persons.items():
        if query.lower() in value["name"].lower():
            results.append({"id": key, **value})
    if not results:
        raise HTTPException(status_code=404, detail="No persons found matching the query")
    return {"persons": results}

@app.get("/get-person")
def get_person(id: str = Query(..., min_length=1)):
    results = []
    for key, value in persons.items():
        if id == value["id"]:
            results.append(value)
            break
    if not results:
        raise HTTPException(status_code=404, detail="No person found matching the ID")
    return(results)

@app.get("/search-organisation", response_model=Dict[str, List[Dict[str, str]]])
def search_person(query: str = Query(..., min_length=1)):
    results = []

    for key, value in organisations.items():
        if (query.lower() in value["sv"].lower()) or ((query.lower() in value["en"].lower()) if ("en" in value) else False):
            results.append({"id": key, **value})
    if not results:
        raise HTTPException(status_code=404, detail="No organisations found matching the query")
    return {"organisations": results}

@app.get("/get-organisation")
def get_organisation(id: str = Query(..., min_length=1)):
    results = []
    for key, value in organisations.items():
        if id == value["id"]:
            results.append(value)
            break
    if not results:
        raise HTTPException(status_code=404, detail="No organisation found matching the ID")
    return(results)