import json
from collections import Counter
import os

"""
Ce script sert à creer les lignes d'insertions concernant les scrutins
dans la base et dans le ficheir data/scrutins.sql

Schéma de table concerant les scrutins:
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


Il manque à chaque fois les 12 mêmes éléments
"""
listeElemRef = ["uid", "numero", "organeRef", "legislature", "sessionRef", "seanceRef", "dateScrutin", "quantiemeJourSeance", "codeTypeVote", "libelleTypeVote", "typeMajorite", "sortCode", "sortLibelle", "titre", "demandeur", "modePublicationDesVotes", "nombreVotants", "suffragesExprimes", "nbrSuffragesRequis", "pour", "contre", "abstention", "nonVotantsVolontaires"]



def escapeString(strings):
    for key in strings:
        value = strings[key]
        if isinstance(value, str):
            # Remplacer chaque "'" par "''"
            strings[key] = value.replace("'", "''")
            strings[key] = strings[key].replace("\r", " - ")
    return strings
   
   

def generateInsert(data, file):
    insertions = {}
    insertions_votes = {}
    try:
        insertions["uid"] = data["scrutin"]["uid"]
        insertions["numero"] = data["scrutin"]["numero"]
        insertions["organeRef"] = data["scrutin"]["organeRef"]
        insertions["legislature"] = data["scrutin"]["legislature"]
        insertions["sessionRef"] = data["scrutin"]["sessionRef"]
        insertions["seanceRef"] = data["scrutin"]["seanceRef"]
        insertions["dateScrutin"] = data["scrutin"]["dateScrutin"]
        insertions["quantiemeJourSeance"] = data["scrutin"]["quantiemeJourSeance"]
        insertions["codeTypeVote"] = data["scrutin"]["typeVote"]["codeTypeVote"]
        insertions["libelleTypeVote"] = data["scrutin"]["typeVote"]["libelleTypeVote"]
        insertions["typeMajorite"] = data["scrutin"]["typeVote"]["typeMajorite"]
        insertions["sortCode"] = data["scrutin"]["sort"]["code"]
        insertions["sortLibelle"] = data["scrutin"]["sort"]["libelle"]
        insertions["titre"] = data["scrutin"]["titre"]
        insertions["demandeur"] = data["scrutin"]["demandeur"]["texte"]
        #print("--------------------------- : ", insertions["demandeur"])
        insertions["modePublicationDesVotes"] = data["scrutin"]["modePublicationDesVotes"]
        insertions["nombreVotants"] = data["scrutin"]["syntheseVote"]["nombreVotants"]
        insertions["suffragesExprimes"] = data["scrutin"]["syntheseVote"]["suffragesExprimes"]
        insertions["nbrSuffragesRequis"] = data["scrutin"]["syntheseVote"]["nbrSuffragesRequis"]
        insertions["pour"] = data["scrutin"]["syntheseVote"]["decompte"]["pour"]
        insertions["contre"] = data["scrutin"]["syntheseVote"]["decompte"]["contre"]
        insertions["abstention"] = data["scrutin"]["syntheseVote"]["decompte"]["abstentions"]
        insertions["nonVotantsVolontaires"] = data["scrutin"]["syntheseVote"]["decompte"]["nonVotantsVolontaires"]
    except KeyError as e:
        print(f"La clé n'a pas été trouvé dans le fichier {file}: ", e)
    
    insertions = escapeString(insertions)
    keys = ""
    values = ""
    for key, value in insertions.items():
        keys = keys + key + ", "
        values = values + "'" + str(value) + "', "
    
    # on enlève le dernier ", " de keys et values
    keys = keys[:-2]
    values = values[:-2]
        
    ret = "INSERT INTO Scrutin (" + keys + ") VALUES (" + values + ");"
   
    #ret = "INSERT INTO Scrutin (", ", ".join(liste_keys), ") VALUES (", ", ".join(["'" + str(value) + "'" if isinstance(value, str) else str(value) for value in liste_values]), ");"
    return str(ret)


def addStringInFile(string, file):
    with open(file, "a", encoding="UTF-8") as f:
        f.write(string + "\n")

folderPath = "json"

file_list = [entry for entry in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, entry))]

nbFiles = len(file_list)
listeAjout = []
for index, file_name in enumerate(file_list):
    with open(folderPath + "/" + file_name, 'r') as file :
        data = json.load(file)
        print("---------------------------")
        print(folderPath + "/" + file_name, index + 1, nbFiles)
        string = generateInsert(data, file_name)
        if string not in listeAjout: # Pour ne pas ajouter deux fois le même scrutin
            listeAjout.append(string)
            addStringInFile(string, "data/scrutins.sql")
        print("---------------------------")

