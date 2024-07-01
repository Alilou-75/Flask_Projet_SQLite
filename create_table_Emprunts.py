import sqlite3

def create_table(db_name):
    # Ouvrir une connexion à la base de données SQLite
    conn = sqlite3.connect(db_name)
    
    # Créer un curseur pour exécuter les commandes SQL
    cursor = conn.cursor()
    
   # Exécuter la commande pour créer la table Emprunts
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
           ID_emprunt INTEGER PRIMARY KEY,
           ID_user INTEGER,
           ID_livre INTEGER,
           Date_emprunt DATE,
           Date_retour_prevue DATE,
           Date_retour_effective DATE,
           FOREIGN KEY (ID_user) REFERENCES Utilisateurs(ID_user),
           FOREIGN KEY (ID_livre) REFERENCES Livres(ID_livre)
        )
    ''')
   
    # Sauvegarder les changements
    conn.commit()
    
    # Fermer la connexion à la base de données
    conn.close()

if __name__ == "__main__":
    db_name = 'database2.db'
    create_table(db_name)
    print(f"La table 'Emprunts' a été créée avec succès dans la base de données '{db_name}'.")


