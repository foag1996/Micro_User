from typing import Union
import requests
from fastapi import FastAPI, status, Response

from fastapi import FastAPI

app = FastAPI()


# @app.get("/")
# def read_root():
#     url = 'https://62f6640ba3bce3eed7c04b72.mockapi.io/items'
#     response = requests.get(url, {}, timeout=5)
#     return {"items": response.json() }


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


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