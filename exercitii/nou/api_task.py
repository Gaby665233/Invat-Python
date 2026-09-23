from fastapi import FastAPI
from functii_task import lista_taskuri, adauga_task_nou, sterge_task_dupa_id
app = FastAPI()

@app.get("/task")
def afiseaza_taskuri():
    return lista_taskuri

@app.post("/create")
def creeaza_task (id:int, titlu:str):
    mesaj = adauga_task_nou(id, titlu)
    return {"status": "Succes", "detalii": mesaj}

@app.delete("/delete")
def sterge_task(id: int):
    mesaj = sterge_task_dupa_id(id)
    return {"status": "Succes", "detalii": mesaj}
    