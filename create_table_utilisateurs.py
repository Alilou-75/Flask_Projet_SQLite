import sqlite3

def create_table(db_name):
    # Ouvrir une connexion à la base de données SQLite
    conn = sqlite3.connect(db_name)
    
    # Créer un curseur pour exécuter les commandes SQL
    cursor = conn.cursor()
    
    # Exécuter la commande pour créer la table utilisateurs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
           ID_user INTEGER PRIMARY KEY AUTOINCREMENT,
           Created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            Nom TEXT NOT NULL,
            Prenom TEXT NOT NULL,
            Adresse TEXT NOT NULL,
            Date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
   
    # Sauvegarder les changements
    conn.commit()
    
    # Fermer la connexion à la base de données
    conn.close()

if __name__ == "__main__":
    db_name = 'database2.db'
    create_table(db_name)
    print(f"La table 'utilisateurs' a été créée avec succès dans la base de données '{db_name}'.")
   
