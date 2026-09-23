# exemplu
def salută_utilizator(nume):
    rezultat = f"Salutare, {nume}!"
    return rezultat

# Aici APELĂM (folosim) funcția
mesaj = salută_utilizator("Gabi")
print(mesaj)  # Va afișa: Salutare, Gabi!


def adunare (a,b):
    return a + b

suma = adunare(10,15)
print(suma)

def este_par(numar):
    return numar % 2 == 0
numar = este_par(4)
print(numar)

def calculeaza_medie(note):
    suma_notelor = sum(note)
    numar_note = len(note)
    media = suma_notelor / numar_note
    return media

note_elev = [10,9,8,7]
rezultat = calculeaza_medie(note_elev)
print(rezultat)


def calculeaza_total_cos(preturi):
    suma = sum(preturi)
    if suma > 200:
        reducere = suma * 0.1
        final = suma - reducere
        return final
    else:
        suma
    

cos_cumparaturi = [50,100,80,20]
rezultat = calculeaza_total_cos(cos_cumparaturi)
print(rezultat)





    
