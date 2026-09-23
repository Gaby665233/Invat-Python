import sqlite3

conexiune = sqlite3.connect("companie.db")
cursor = conexiune.cursor()

# Codul de creare (rămâne neschimbat)
cursor.execute("""
CREATE TABLE IF NOT EXISTS angajati (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nume TEXT,
    job TEXT,
    salariu INTEGER
)
""")

# --- AICI ESTE CODUL NOU DE INSERARE ---
# Pregătim comanda SQL cu ? în loc de valori directe
comanda_sql = "INSERT INTO angajati (nume, job, salariu) VALUES (?, ?, ?)"

# Datele pe care vrem să le inserăm (sub formă de tuplu, între paranteze rotunde)
date_angajat = ("Andrei", "Developer", 4500)

# Executăm comanda trimițând și datele
cursor.execute(comanda_sql, date_angajat)
# ----------------------------------------


# --- CODUL DE CITIRE/SELECT ---
# Executăm comanda SQL de selectare
cursor.execute("SELECT * FROM angajati")

# Luăm toate rândurile din baza de date
toti_angajatii = cursor.fetchall()

# Trecem prin fiecare rând cu un loop și îl printăm
for angajat in toti_angajatii:
    print(angajat)
# ------------------------------

# La SELECT nu este neapărat nevoie de conexiune.commit(), dar închiderea e obligatorie
conexiune.close()