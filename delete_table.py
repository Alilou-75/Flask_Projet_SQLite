import sqlite3

def drop_table(db_name, table_name):
    # Ouvrir une connexion à la base de données SQLite
    conn = sqlite3.connect(db_name)
    
    # Créer un curseur pour exécuter les commandes SQL
    cursor = conn.cursor()
    
    # Exécuter la commande pour supprimer la table
    cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
    
    # Sauvegarder les changements
    conn.commit()
    
    # Fermer la connexion à la base de données
    conn.close()

if __name__ == "__main__":
    db_name = 'database2.db'
    table_name = 'utilisateurs'
    
    drop_table(db_name, table_name)
    print(f"Table '{table_name}' supprimée avec succès de la base de données '{db_name}'.")
