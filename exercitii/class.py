class angajat:
    def __init__(self, nume, job, salariu):
        self.nume = nume
        self.job = job
        self.salariu = salariu
    def afiseaza_detalii(self):
        print(f" {self.nume} lucrează ca {self.job} și are un salariu de {self.salariu} lei")

angajat1 = angajat ("Gabi", "python", "3000" )
angajat1.afiseaza_detalii()