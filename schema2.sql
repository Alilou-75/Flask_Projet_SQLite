DROP TABLE IF EXISTS livres;
CREATE TABLE livres (
    ID_livre INTEGER PRIMARY KEY AUTOINCREMENT,
    Titre VARCHAR(255),
    Auteur VARCHAR(255),
    Annee_publication INTEGER,
    Quantite INTEGER
);

CREATE TABLE Utilisateurs (
    ID_utilisateur INTEGER PRIMARY KEY,
    Nom VARCHAR(255),
    Prenom VARCHAR(255),
    Email VARCHAR(255),
    Date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Emprunts (
    ID_emprunt INTEGER PRIMARY KEY,
    ID_utilisateur INTEGER,
    ID_livre INTEGER,
    Date_emprunt DATE,
    Date_retour_prevue DATE,
    Date_retour_effective DATE,
    FOREIGN KEY (ID_utilisateur) REFERENCES Utilisateurs(ID_utilisateur),
    FOREIGN KEY (ID_livre) REFERENCES Livres(ID_livre)
);
