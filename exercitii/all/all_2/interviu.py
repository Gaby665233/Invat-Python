# Un magazin vrea să trimită un e-mail clienților săi fideli./n
#  Ai o listă cu dicționare care conține clienții și sumele cheltuite de ei:

clienti = [
    {"nume": "Ina", "cheltuit": 150},
    {"nume": "Marius", "cheltuit": 450},
    {"nume": "Daria", "cheltuit": 90},
    {"nume": "Vlad", "cheltuit": 600}
]

filtrare_clienti = [x["nume"] for x in clienti if x["cheltuit"] > 200]
print(filtrare_clienti)