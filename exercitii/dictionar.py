laptop = {
    "marca": "Lg",
    "pret": 2000,
    "este_nou": True

}
print(laptop["marca"])

laptop["pret"] = 1500
laptop["culoare"] = "argintiu"

print(laptop)

utilizatori = [
    {"nume": "Ion", "varsta": 17},
    {"nume": "Maria", "varsta": 22},
    {"nume": "George", "varsta": 15}
]
for i in utilizatori:
    if i["varsta"] >= 18:
        print(f" {i["nume"]} ai peste 18 ani")
    else:
        print(f"{i["nume"]} nu ai voie sa intri")