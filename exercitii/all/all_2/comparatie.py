# Modul vechi și lung (cu 3 linii de cod):
numere = [1, 2, 3]
rezultat = []
for x in numere:
    rezultat.append(x * 10)
print(rezultat)

# Varianta mult mai bune 
numere = [1, 2, 3]
rezultat = [x * 10 for x in numere] # Citește-l de la dreapta la stânga!
print(rezultat) 

