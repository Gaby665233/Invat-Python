# with open("agenda.txt", "a") as fisier:
#     fisier.write("Andrei: 0722123456\n")

# with open("agenda.txt", "r") as fisier:
#     continut = fisier.read()
#     print(continut)

while True:
    try:
        pret = float(input("introdu pretul "))
        TVA = pret * 0.19
        with open("vaazari.txt", "a") as fisier:
            fisier.write(f"Produsul costa {pret} lei, iar pretul cu TVA este {pret + TVA}\n")
        
    except ValueError:
        print("Prețul introdus este incorect!") 
