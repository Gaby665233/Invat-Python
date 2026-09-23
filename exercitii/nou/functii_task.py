lista_taskuri = []


def adauga_task_nou(id_task, titlu_task):
    task = {
        "id": id_task,
        "titlu": titlu_task,
        "terminal": False
    }
    lista_taskuri.append(task)
    return "Task adăugat cu succes!"

def sterge_task_dupa_id(id_cautat):
    global lista_taskuri
    lista_taskuri = [x for x in lista_taskuri if x["id"] != id_cautat]
    

       
        