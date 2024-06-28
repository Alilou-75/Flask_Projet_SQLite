import sqlite3

   connection = sqlite3.connect('database2.db')

with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Création de la table 'livres'
cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)",(1, 'Emilie', 'Victor', 2024, 10))
cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)",(2, 'Didier', 'Laurent', 2023, 5))

# Création de la table 'utilisateurs'
cur.execute("INSERT INTO utilisateurs (ID_user, nom, prenom, adresse) VALUES (?, ?, ?, ?)",(1, 'SELLAM', 'Ali', '239, avenue Gambetta, 75020 Paris'))
cur.execute("INSERT INTO utilisateurs (ID_user, nom, prenom, adresse) VALUES (?, ?, ?, ?)",(2, 'LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'))
cur.execute("INSERT INTO utilisateurs (ID_user, nom, prenom, adresse) VALUES (?, ?, ?, ?)",(3, 'MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'))
cur.execute("INSERT INTO utilisateurs (ID_user, nom, prenom, adresse) VALUES (?, ?, ?, ?)",(4, 'LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris'))

# Création de la table 'emprunts'
cur.execute("INSERT INTO emprunts (ID_emprunt, ID_user, ID_livre, date_emprunt, Date_retour_prevue, Date_retour_effective ) VALUES (?, ?, ?, ?, ?, ?)",(1, 1, 1))


conn.commit()
conn.close()
