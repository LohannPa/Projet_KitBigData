import os
from modules.gestion_des_taches import GestionnaireTaches


nom_fichier_data = 'data_taches.csv'

dossier_data = os.path.join(os.path.dirname(__file__), 'data')

chemin_fichier_csv = os.path.join(dossier_data,nom_fichier_data )


# Exemple d'utilisation
if __name__ == "__main__":
    gestionnaire = GestionnaireTaches(chemin_fichier_csv)
    gestionnaire.ajouter_tache("tache1", "Description de la tâche 1")
    gestionnaire.ajouter_tache("tache2", "Description de la tâche 2")