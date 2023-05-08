from typing import Union, List

from fastapi import FastAPI, Request, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

class Data:
    def __init__(self):
        self.data = {"data": [
        {
            "name": "Fernando Alonso",
            "score": 15,
            "team": "Aston Martin",
            "logo": "aston.png",
            "flag": "spain.png"
        },
        {
            "name": "Sergio Perez",
            "score": 12,
            "team": "Redbull",
            "logo": "redbull.png",
            "flag": "mexico.png"
        },
        {
            "name": "Carlos sainz Jr.",
            "score": 10,
            "team": "Ferrari",
            "logo": "ferrari.png",
            "flag": "spain.png"
        },
        {
            "name": "Max Verstappen",
            "score": 25,
            "team": "Redbull",
            "logo": "redbull.png",
            "flag": "netherlands.png"
        },
        {
            "name": "Lance Stroll",
            "score": 8,
            "team": "Aston Martin",
            "logo": "aston.png",
            "flag": "canada.png"
        },
        {
            "name": "Lewis Haimlton",
            "score": 6,
            "team": "Mercedes AMG",
            "logo": "amg.png",
            "flag": "england.png"
        },
        {
            "name": "Charles Leclerc",
            "score": 18,
            "team": "Ferrari",
            "logo": "ferrari.png",
            "flag": "monaco.png"

        },
        {
            "name": "George Rusell",
            "score": 4,
            "team": "Mercedes AMG",
            "logo": "amg.png",
            "flag": "england.png"

        },
        {
            "name": "Kevin Magnussen",
            "score": 2,
            "team": "Haas",
            "logo": "haas.png",
            "flag": "denmark.png"
        },
        {
            "name": "Lando Norris",
            "score": 1,
            "team": "McLaren",
            "logo": "mclaren.png",
            "flag": "england.png"
        }]}

    def setData(self, dataI):
        self.data = dataI

data = Data()


class Item(BaseModel):
    name: str
    score: int 
    team: str
    logo: str
    flag: str

class ListItem(BaseModel):
    data: List[Item]



@app.get("/points")
def read_root():
    print(data.data)
    return data.data


@app.post("/items")
def read_item(info : ListItem):
    data.setData(info.dict())
    return {"response": "OK"}