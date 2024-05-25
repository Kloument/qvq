import csv
import mysql.connector
"""
Création des lignes d'insertions de personnes dans le fichier insertionPersonneLignes.sql 
avec le bon id du grp politique

destination : data/insertionPersonneLignes.sql
"""

def recupUidGroupe(NomGrpAbrege) :
    listeUidGrp = [['PO266900', 'NI'], ['PO270907', 'SOC'], ['PO730934', 'LR'], ['PO774834', 'Dem'], ['PO800490', 'LFI - NUPES'], ['PO800502', 'GDR - NUPES'], ['PO800514', 'HOR'], ['PO800520', 'RN'], ['PO800526', 'Ecolo - NUPES'], ['PO800532', 'LIOT'], ['PO800538', 'RE']]
    for uidGrp in listeUidGrp :
        if uidGrp[1] == NomGrpAbrege :
            return uidGrp[0]



def insertionPersonne() : 

    # Chemin vers le fichier CSV
    chemin_fichier_csv = "data/liste_deputes.csv"

    nom_table_sql = "Personne"
    # Ouvrir le fichier CSV en mode lecture
    with open(chemin_fichier_csv, newline='', encoding='utf-8') as csvfile:
        # Créer un objet lecteur CSV
        lecteur_csv = csv.reader(csvfile, delimiter=',', )
        
        # Ignorer l'en-tête si nécessaire
        header = next(lecteur_csv)
        
        # Itérer sur chaque ligne du fichier CSV
        i = 1
        for ligne in lecteur_csv:
            # Générer la requête SQL INSERT INTO
            # en utilisant les données de la ligne

            grpAbgre = ligne[8]

            uidGrp = recupUidGroupe(grpAbgre)
            id = ligne[0].replace("'", "''")
            id = "PA" + id
            prenom = ligne[1].replace("'", "''") 
            nom = ligne[2].replace("'", "''")
            region = ligne[3].replace("'", "''")
            departement = ligne[4].replace("'", "''")
            profession = ligne[6].replace("'", "''")
            numeroCirconscription = ligne[5]

            requete_sql = f"INSERT INTO {nom_table_sql} (uid, prenom, nom, region, departement, numeroCirconscription, profession, groupe) VALUES ('{id}', '{prenom}', '{nom}', '{region}', '{departement}', {numeroCirconscription}, '{profession}', '{uidGrp}');"
                
            # Afficher la requête SQL (ou l'exécuter dans une base de données)
            with open('data/insertionPersonneLignes.sql', 'a', encoding='utf-8') as file:
                print(f"{i} : ligne ajoutée : ", requete_sql)
                file.write(requete_sql + '\n')
                i += 1

            #print(requete_sql)


insertionPersonne()
