-- insertion des groupes

/*
Liste des groupes :
['Horizons et apparentés'
 'Libertés, Indépendants, Outre-mer et Territoires'
 'La France insoumise - Nouvelle Union Populaire écologique et sociale'
 'Renaissance' 'Démocrate (MoDem et Indépendants)'
 'Rassemblement National' 'Socialistes et apparentés'
 'Gauche démocrate et républicaine - NUPES' 'Les Républicains'
 'Écologiste - NUPES' 'Non inscrit']

 Liste des groupe abrégé :
 ['HOR' 'LIOT' 'LFI - NUPES' 'RE' 'Dem' 'RN' 'SOC' 'GDR - NUPES' 'LR'
 'Ecolo - NUPES' 'NI']

 Liste des groupes avec leur uid: 
 [['PO266900', 'NI'], ['PO270907', 'SOC'], ['PO730934', 'LR'], ['PO774834', 'Dem'], ['PO800490', 'LFI - NUPES'], ['PO800502', 'GDR - NUPES'], ['PO800514', 'HOR'], ['PO800520', 'RN'], ['PO800526', 'Ecolo - NUPES'], ['PO800532', 'LIOT'], ['PO800538', 'RE']]

*/
INSERT INTO Groupe (uid, groupeComplet, groupeAbrege) VALUES ('PO266900', 'Non inscrit', 'NI');
INSERT INTO Groupe (uid, groupeComplet, groupeAbrege) VALUES ('PO270907', 'Socialistes et apparentés', 'SOC');
INSERT INTO Groupe (uid, groupeComplet, groupeAbrege) VALUES ('PO730934', 'Les Républicains', 'LR');
INSERT INTO Groupe (uid, groupeComplet, groupeAbrege) VALUES ('PO774834', 'Démocrate (MoDem et Indépendants)', 'Dem');
INSERT INTO Groupe (uid, groupeComplet, groupeAbrege) VALUES ('PO800490', 'La France insoumise - Nouvelle Union Populaire écologique et sociale', 'LFI - NUPES');
INSERT INTO Groupe (uid, groupeComplet, groupeAbrege) VALUES ('PO800502', 'Gauche démocrate et républicaine - NUPES', 'GDR - NUPES');
INSERT INTO Groupe (uid, groupeComplet, groupeAbrege) VALUES ('PO800514', 'Horizons et apparentés', 'HOR');
INSERT INTO Groupe (uid, groupeComplet, groupeAbrege) VALUES ('PO800520', 'Rassemblement National', 'RN');
INSERT INTO Groupe (uid, groupeComplet, groupeAbrege) VALUES ('PO800526', 'Écologiste - NUPES', 'Ecolo - NUPES');
INSERT INTO Groupe (uid, groupeComplet, groupeAbrege) VALUES ('PO800532', 'Libertés, Indépendants, Outre-mer et Territoires', 'LIOT');
INSERT INTO Groupe (uid, groupeComplet, groupeAbrege) VALUES ('PO800538', 'Renaissance', 'RE');
