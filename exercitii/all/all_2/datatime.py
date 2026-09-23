from datetime import datetime

acum = datetime.now()
print(acum)

print(acum.year)  # Afișează doar anul (ex: 2026)
print(acum.day)

format_frumos = acum.strftime("%d-%m-%Y %H:%M")
print(format_frumos) 