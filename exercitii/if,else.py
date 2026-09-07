numar = -5

if numar >= 0:
    print("Numarul este pozitiv")
else:
    print("Numarul este negativ")


ora = 14

if ora < 12:
    print("Buna dimineata")
elif 12 <= ora <= 18:
    print("Buna ziua")
else:
    print("buna seara")

pret = 150
are_cupon = True
nu_are_cupon = False

pret_reducere = 150 * 0.2
print(pret_reducere)
pret_de_platit = pret - pret_reducere
print( pret_de_platit)
print(f"Clientul plateste {pret_de_platit} avand reducere {are_cupon}")
# varainta cu if
# verificam daca are reducere

if are_cupon:
    pret * 150
    pret_de_plati = pret - pret_reducere
else:
    pret_de_plati = pret
print(f"Clientul plateste {pret_de_plati}")
