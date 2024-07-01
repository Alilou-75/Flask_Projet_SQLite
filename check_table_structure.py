import sqlite3

def check_table_structure(db_name, table_name):
    # Ouvrir une connexion à la base de données SQLite
    conn = sqlite3.connect(db_name)
    
    # Créer un curseur
    cursor = conn.cursor()
    
    # Exécuter une commande SQL pour afficher la structure de la table
    cursor.execute(f'PRAGMA table_info({table_name})')
    
    # Récupérer les résultats
    columns = cursor.fetchall()
    
    # Afficher les résultats
    print(f"Structure de la table '{table_name}':")
    for column in columns:
        print(column)
    
    # Fermer la connexion à la base de données
    conn.close()

if __name__ == "__main__":
    # Nom de la base de données et de la table à vérifier
    db_name = 'database2.db'
    table_name = 'Emprunts'
    
    check_table_structure(db_name, table_name)
