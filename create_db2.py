import sqlite3

    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()

   # Création de la table 'livres'
cursor.execute('''
CREATE TABLE IF NOT EXISTS livres (
    ID_livre INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT,
    auteur TEXT,
    annee_publication INTEGER,
    quantite INTEGER
)
''')

# Création de la table 'utilisateurs'
cursor.execute('''
CREATE TABLE IF NOT EXISTS utilisateurs (
    ID_user INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    prenom TEXT,
    adresse TEXT,
    Date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Création de la table 'emprunts'
cursor.execute('''
CREATE TABLE IF NOT EXISTS emprunts (
    ID_emprunt INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_user INTEGER,
    ID_livre INTEGER,
    date_emprunt TEXT,
    FOREIGN KEY (ID_user) REFERENCES utilisateurs (ID_user),
    FOREIGN KEY (ID_livre) REFERENCES livres (ID_livre)
)
''')

conn.commit()
conn.close()
