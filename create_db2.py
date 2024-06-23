import sqlite3

def create_database():
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()

    # Table des livres
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livres (
            ID_livre INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            auteur TEXT NOT NULL,
            annee_publication INTEGER NOT NULL,
            quantite INTEGER NOT NULL
        )
    ''')

    # Table des utilisateurs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
            ID_utilisateur INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    # Table des emprunts
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emprunts (
            ID_emprunt INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_utilisateur INTEGER NOT NULL,
            ID_livre INTEGER NOT NULL,
            date_emprunt TEXT NOT NULL,
            date_retour TEXT,
            FOREIGN KEY (ID_utilisateur) REFERENCES utilisateurs(ID_utilisateur),
            FOREIGN KEY (ID_livre) REFERENCES livres(ID_livre)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    print("Les bases de données ont été créées avec succès.")
