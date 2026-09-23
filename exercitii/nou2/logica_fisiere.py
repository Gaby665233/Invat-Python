from fastapi import FastAPI
from api_fisiere import verifica_fisier

app = FastAPI()

@app.post("/upload")
def afisare_document(nume_document: str):
    if verifica_fisier(nume_document) == True:
        return{"status": "Succes", "mesaj": "Fișierul a fost încărcat!"}
    else:
        return{"status": "Eroare", "mesaj": "Tip de fișier interzis!"}
     
    