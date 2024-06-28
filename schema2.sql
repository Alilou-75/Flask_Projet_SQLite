DROP TABLE IF EXISTS livres;
CREATE TABLE livres (
    ID_livre INTEGER PRIMARY KEY AUTOINCREMENT,
    Titre VARCHAR(255),
    Auteur VARCHAR(255),
    Annee_publication INTEGER,
    Quantite INTEGER
);
DROP TABLE IF EXISTS Utilisateurs;
CREATE TABLE Utilisateurs (
    ID_user INTEGER PRIMARY KEY,
    Nom VARCHAR(255),
    Prenom VARCHAR(255),
    Adresse VARCHAR(255),
    Date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
DROP TABLE IF EXISTS Emprunts;
CREATE TABLE Emprunts (
    ID_emprunt INTEGER PRIMARY KEY,
    ID_user INTEGER,
    ID_livre INTEGER,
    Date_emprunt DATE,
    Date_retour_prevue DATE,
    Date_retour_effective DATE,
    FOREIGN KEY (ID_user) REFERENCES Utilisateurs(ID_user),
    FOREIGN KEY (ID_livre) REFERENCES Livres(ID_livre)
);
