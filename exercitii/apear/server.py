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


@app.post("/adauga")
def adauga_angajat(nume: str, job: str, salariu: int):
    # Deschiem fișierul în modul "a" (Append / Adăugare)
    with open("date_angajati.txt", "a") as fisier:
        # \n la final este obligatoriu ca următorul angajat să treacă pe rând nou!
        fisier.write(f"{nume},{job},{salariu}\n")
        
    return {"status": "Succes", "mesaj": f"Angajatul {nume} a fost adăugat în fișier!"}

       