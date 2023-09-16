# Para correr el servidor: uvicorn server:app --reload
# se debe instalar uvicorn: pip install uvicorn
# se debe instalar FastAPI: pip install fastapi
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from paquete.cola import Cola

app = FastAPI()
cola = Cola()

@app.get("/")
def read_root():
    return {"Hello": "World", "estado": True}

@app.get("/estado")
def estado():
    elementos = cola.contar()
    return {"status": "ok", "elementos": elementos}

@app.post("/encolar")
def encolar(item: dict):
    cola.encolar(item)
    return {"status": "ok", "metodo": "encolar"}

@app.get("/desencolar")
def desencolar():
    elemento = cola.desencolar()
    return {"status": "ok", "elemento": elemento}

@app.get("/ver_todos")
def ver_todos():
    elementos = cola.ver_listado()
    return {"status": "ok", "elementos": elementos}