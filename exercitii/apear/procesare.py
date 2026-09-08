with open ("exercitii/apear/date_angajati.txt", "r") as fisier:
    for linie in fisier: 
        bucati = linie.strip().split(",") 
        print(f"Angajatul {bucati[0]} lucrează ca {bucati[1]} și are salariul de {bucati[2]} lei.") 

         