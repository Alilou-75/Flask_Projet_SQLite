import sqlite3

   connection = sqlite3.connect('database2.db')

with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Création de la table 'livres'
cur.execute("INSERT INTO Livres (Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?)",('Emilie', 'Victor', 2024, 10))
cur.execute("INSERT INTO Livres (Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?)",('Didier', 'Laurent', 2023, 5))

# Création de la table 'utilisateurs'
cur.execute("INSERT INTO utilisateurs (nom, prenom, adresse) VALUES (?, ?, ?)",('SELLAM', 'Ali', '239, avenue Gambetta, 75020 Paris'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, adresse) VALUES (?, ?, ?)",('LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, adresse) VALUES (?, ?, ?)",('MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, adresse) VALUES (?, ?, ?)",('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris'))

# Création de la table 'emprunts'
cur.execute("INSERT INTO emprunts (ID_emprunt, ID_user, ID_livre, date_emprunt, Date_retour_prevue, Date_retour_effective ) VALUES (?, ?, ?, ?, ?, ?)",(1, 1, 1))


conn.commit()
conn.close()
