#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base de données
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()

    # Exécution de la requête SELECT
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Affichage des résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
