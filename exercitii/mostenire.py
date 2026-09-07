# Clasa Părinte
class Animal:
    def mananca(self):
        print("Acest animal mănâncă.")

# Clasa Copil (punem părintele în paranteze)
class Caine(Animal):
    def latra(self):
        print("Ham ham!")

# Câinele are și metoda lui, DAR o moștenește și pe cea de la Animal
grivei = Caine()
grivei.mananca()  # Afișează: Acest animal mănâncă.
grivei.latra()    # Afișează: Ham ham!


class angajat:
    def __init__(self, nume, job, salariu):
        self.nume = nume
        self.job = job
        self.salariu = salariu
    def afiseaza_detalii(self):
        print(f" {self.nume} lucrează ca {self.job} și are un salariu de {self.salariu} lei")

class manager(angajat):
    def ofer_bonus(self,suma_bonus):
        
        print(f"Managerul {self.nume} a oferit un bonus de {suma_bonus} lei echipei sale")


angajat1 = angajat ("Gabi", "python", "3000" )
angajat1.afiseaza_detalii()

manager1 = manager ("Alex", "manager Ts", "2000")
manager1.afiseaza_detalii()
manager1.ofer_bonus(500)
