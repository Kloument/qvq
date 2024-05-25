/*
Base de donnes mysql
Création de la base de données qvq
*/
-- CREATE DATABASE IF NOT EXISTS qvq;
-- USE qvq;

-- table : Groupe
CREATE TABLE Groupe (
    -- id INT AUTO_INCREMENT,
    uid VARCHAR(255) NOT NULL UNIQUE,
    groupeComplet VARCHAR(255) NOT NULL UNIQUE,
    groupeAbrege VARCHAR(255) NOT NULL UNIQUE,
    CONSTRAINT pk_Groupe PRIMARY KEY (uid)
);

-- Table: Personne
CREATE TABLE Personne (
    -- id INT AUTO_INCREMENT,
    uid VARCHAR(255),
    prenom VARCHAR(255),
    nom VARCHAR(255),
    region VARCHAR(255),
    departement VARCHAR(255),
    numeroCirconscription VARCHAR(255),
    profession VARCHAR(255),
    groupe VARCHAR(255),
    CONSTRAINT pk_Personne PRIMARY KEY (uid),
    CONSTRAINT fk_Groupe_Personne FOREIGN KEY (groupe) REFERENCES Groupe(uid)
);

-- Table: Scrutin
CREATE TABLE Scrutin (
    uid VARCHAR(255),
    numero INT,
    organeRef VARCHAR(255),
    legislature INT,
    sessionRef VARCHAR(255),
    seanceRef VARCHAR(255),
    dateScrutin DATE,
    quantiemeJourSeance INT,
    codeTypeVote VARCHAR(255),
    libelleTypeVote VARCHAR(255),
    typeMajorite VARCHAR(255),
    sortCode VARCHAR(255),
    sortLibelle VARCHAR(255),
    titre TEXT,
    demandeur TEXT,
    modePublicationDesVotes VARCHAR(255),
    nombreVotants INT,
    suffragesExprimes INT,
    nbrSuffragesRequis INT,
    pour INT,
    contre INT,
    abstention INT,
    nonVotantsVolontaires INT,
    CONSTRAINT pk_Scrutin PRIMARY KEY (uid)
);

CREATE TABLE Vote (
    id INT AUTO_INCREMENT PRIMARY KEY,
    scrutin_id VARCHAR(255),
    personne_id VARCHAR(255),
    choix_vote ENUM('pour', 'contre', 'abstention') NOT NULL,
    mandat_ref VARCHAR(255),
    CONSTRAINT fk_Vote_Scrutin FOREIGN KEY (scrutin_id) REFERENCES Scrutin(uid),
    CONSTRAINT fk_Vote_Personne FOREIGN KEY (personne_id) REFERENCES Personne(uid)
);


/*
Création de l'utilisateur bobSelect
qui ne peut que faire des SELECT mais depuis n'importe quelle adresse IP
*/
CREATE USER 'bobSelect'@'%' IDENTIFIED BY 'p8G^`v_%$<(m.a^e1|5j';
GRANT SELECT ON qvq.* TO 'bobSelect'@'%';
FLUSH PRIVILEGES;


