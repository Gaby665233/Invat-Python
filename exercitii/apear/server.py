from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def pagina_principala():
    lista_angajati = []
    with open("date_angajati.txt", "r") as fisier:
      for linie in fisier:
        bucati = linie.strip().split(",")
        persoane = {
           "nume": bucati[0],
            "job": bucati[1],
            "salariu": bucati[2]
        }
        lista_angajati.append(persoane)
    return lista_angajati

       