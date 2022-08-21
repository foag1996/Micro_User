from typing import Union
import requests
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI, status, Response

from fastapi import FastAPI

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return infoUser()

@app.get("/infoUser/{idUsuario}")
def read_item(idUsuario : str):
    list=infoUser()
    for item in list:
        if item["idUsuario"]==idUsuario:
            return item
        
    return Response(status_code= status.HTTP_204_NO_CONTENT)


def infoUser():
    url='https://630264749eb72a839d6ef2ff.mockapi.io/infoUsers'
    response = requests.get(url, {}, timeout=5)
    return response.json()

