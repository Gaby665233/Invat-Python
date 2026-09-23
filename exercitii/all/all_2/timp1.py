from datetime import datetime, timedelta

acum = datetime.now()
# Creăm o durată de 7 zile
durata = timedelta(days=7)

# Adunăm durata la data de acum
data_viitoare = acum + durata
print(data_viitoare.strftime("%d-%m-%Y")) # Va afișa data de peste exact o săptămână


from datetime import datetime, timedelta

start_abonament = datetime.now()

durata = timedelta(days = 30)

calcul = start_abonament + durata

expira = calcul.strftime("%d:%m:%Y")

print(f"Abonamentul tău expiră la data de: {expira}")