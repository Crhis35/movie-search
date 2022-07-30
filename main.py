import json
import requests
import urllib3
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from query import search_prefix

app = FastAPI()

urllib3.disable_warnings()


endpoint = 'https://localhost:9200'
username = 'admin'
password = 'admin'

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SearchInput(BaseModel):
    keyword: str


@app.post("/")
async def root(input: SearchInput):
    print(input)
    url = endpoint + '/movies/_search'
    query = search_prefix(input.keyword)
    query = json.dumps(query)
    r = requests.get(url,
                     auth=(username, password),
                     data=query,
                     verify=False,
                     headers={'Content-type': 'application/json'})
    print(r.json())
    return r.json()
