import os
from modules.gestion_des_taches import GestionnaireTaches
from modules.supprimer_taches import SupprimerTache


nom_fichier_data = 'data_taches.csv'

dossier_data = os.path.join(os.path.dirname(__file__), 'data')

chemin_fichier_csv = os.path.join(dossier_data, nom_fichier_data)


# Exemple d'utilisation
if __name__ == "__main__":
    gestionnaire = GestionnaireTaches(chemin_fichier_csv)
    supprimeur = SupprimerTache(gestionnaire)

    gestionnaire.ajouter_tache("tache1", "Description de la tâche 1")
    gestionnaire.ajouter_tache("tache2", "Description de la tâche 2")

    # supprimeur.supprimer_tache("tache1")
    # supprimeur.supprimer_tache("tache2")
