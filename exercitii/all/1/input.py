# try:
#     varsta_text = input("Câți ani ai? ")
#     varsta = int(varsta_text) # Transformăm textul în număr întreg
#     print(f"Peste 10 ani vei avea {varsta + 10} ani.")
# except ValueError:
#     print("Eroare: Te rog să introduci un număr valid, nu litere!")
while True:
    try:
        pret = float(input("introdu pretul "))
        TVA = pret * 0.19
        print(f"Pretul cu TVA este {pret + TVA}")
    except ValueError:
        print("Prețul introdus este incorect!") 
