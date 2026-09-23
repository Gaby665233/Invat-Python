extensii_permise = [".jpg", ".png", ".txt"]

def verifica_fisier(nume_fisier):
    for i in extensii_permise:
        if nume_fisier.endswith(i):
            return True
    return False
            
    