import json
import os


"""
Script pour creer les lignes d'insertions des votes dans la base de données

destination : data/votes.sql

"""


def addStringInFile(string, file):
    with open(file, "a", encoding="UTF-8") as f:
        f.write(string + "\n")

def action(fileName):
    # Ouverture du JSON
    with open(fileName, 'r') as file :
        data = json.load(file)
    
    # Accéder à l'élément "groupe" dans la structure JSON
    groupes = data["scrutin"]["ventilationVotes"]["organe"]["groupes"]["groupe"]

    # Acceder à l'uid du scrutin
    uid = data["scrutin"]["uid"]
    # Boucler sur chaque groupe
    for groupe in groupes:
        #print("----------------------------")
        # Traiter chaque groupe ici
        #print("Groupe : ", groupe["organeRef"])
        # Vous pouvez accéder à d'autres éléments du groupe ici, par exemple "nombreMembresGroupe", "vote", etc.
        #print("Nombre de membres du groupe : ", groupe["nombreMembresGroupe"])
        glob = groupe["vote"]["decompteNominatif"]
        for key in glob:
            #print(key, ":", glob[key])
            personnes = glob[key]
            listePosVote = ["pours", "contres", "abstentions"]
            if personnes != None and key in listePosVote:
                #print("Type de vote : ", key)
                for personne in personnes["votant"]:
                    
                    if isinstance(personne, dict):
                        # Cas ou il y a plusieurs votants donc un dictionnaire
                        #print("C UN DICT")
                        acteur_ref = personne.get("acteurRef")
                        mandat_ref = personne.get("mandatRef")
                        #print(acteur_ref, " - ", mandat_ref, "-->", key[:-1])
                        #Requete d'insertion
                        insert = "INSERT IGNORE INTO Vote (scrutin_id, personne_id, choix_vote, mandat_ref) VALUES ('" + uid + "', '" + acteur_ref + "', '" + key[:-1] + "', '" + mandat_ref + "');"
                        # Utilisation de INSERT IGNORE car certains votes sont associé à des personnes qui ne sont des députés actuel
                        # Car le fichier json contient des votes de députés qui ne sont plus en fonction
                        
                        addStringInFile(insert, "data/votes.sql")
                        #print("fin de l'insertion")
                    elif isinstance(personne, str):
                        # Cas ou il n'y a qu'un seul votant donc un str
                        # Ainsi le for va boucler sur chaque elem (acteurRef et mandatRef, parDelegation)
                        # Donc il faut mettre un break pour par avoir deux fois le même vote
                        #print("C'est un str : ",personnes["votant"])
                        #print(personnes["votant"]["acteurRef"], " - ", personnes["votant"]["mandatRef"], "-->", key[:-1])
                        insert = "INSERT IGNORE INTO Vote (scrutin_id, personne_id, choix_vote, mandat_ref) VALUES ('" + uid + "', '" + personnes["votant"]["acteurRef"] + "', '" + key[:-1] + "', '" + personnes["votant"]["mandatRef"] + "');"
                        addStringInFile(insert, "data/votes.sql")
                        #print("fin de l'insertion")
                        break
                    else:
                        print("AUTRE TYPE : ", type(personne))  
            #else:
                #print("Pas de votants -->", key)



folderPath = "json"

file_list = [entry for entry in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, entry))]

nbFiles = len(file_list)

for index, file_name in enumerate(file_list):
    with open(folderPath + "/" + file_name, 'r') as file :
        data = json.load(file)
        #print("---------------------------")
        print(folderPath + "/" + file_name, index + 1, nbFiles)
        action(folderPath + "/" + file_name)
        #print("---------------------------")