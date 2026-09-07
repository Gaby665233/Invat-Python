import random


#  numar_secret se schimba la introducerea a fiecarei cifre
while True:
    try:
        numar_secret = random.randint(1,10)
        numar_random = int(input("Introdu un numar "))
        if numar_random < numar_secret:
            print("Prea mic! Mai încearcă.")
        elif numar_random > numar_secret:
            print ("Prea mare! Mai încearcă.")
        elif numar_secret == numar_random:
            print("Felicitări! Ai ghicit numărul secret!")
            break
    except ValueError:
        print("Eroare")


# in varianta asta numar_secret ramane acelasi
import random

# Generăm numărul secret O SINGURĂ DATĂ, înainte să înceapă jocul
numar_secret = random.randint(1, 10)

while True:
    try:
        numar_random = int(input("Introdu un numar: "))
        
        if numar_random < numar_secret:
            print("Prea mic! Mai încearcă.")
        elif numar_random > numar_secret:
            print("Prea mare! Mai încearcă.")
        else: # Putem pune direct else, pentru că dacă nu e mai mic și nici mai mare, sigur este egal!
            print("Felicitări! Ai ghicit numărul secret!")
            break
            
    except ValueError:
        print("Eroare: Introdu un număr valid!")