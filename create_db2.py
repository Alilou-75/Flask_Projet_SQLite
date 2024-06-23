import sqlite3

connection = sqlite3.connect('database2.db')

with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)",(1, 'Emilie', 'Victor', 2024, 10))
cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)",(2, 'Didier', 'Laurent', 2023, 5))

cur.execute("INSERT INTO Utilisateurs (nom, prenom, adresse) VALUES (?, ?, ?)",('SELLAM', 'Ali', '239, avenue Gambetta, 75020 Paris'))
cur.execute("INSERT INTO Utilisateurs (nom, prenom, adresse) VALUES (?, ?, ?)",('LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'))
cur.execute("INSERT INTO Utilisateurs (nom, prenom, adresse) VALUES (?, ?, ?)",('MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'))
cur.execute("INSERT INTO Utilisateurs (nom, prenom, adresse) VALUES (?, ?, ?)",('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris'))

connection.commit()
connection.close()
