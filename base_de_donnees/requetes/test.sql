-- Afficher les données de la table Personne sur Marine Le Pen

SELECT * FROM Personne WHERE nom = 'Le Pen' AND prenom = 'Marine';

-- Afficher le nombre de votes pour Marine Le Pen pour l'année 2024
SELECT COUNT(*) FROM Vote JOIN Personne ON Vote.personne_id = Personne.uid JOIN Scrutin ON Scrutin.uid = Vote.scrutin_id WHERE Personne.nom = 'Le Pen' AND Personne.prenom = 'Marine' AND dateScrutin BETWEEN '2024-01-01' AND '2024-12-31';




