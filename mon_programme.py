"""
Imports et exemple d'utilisation des modules de gestion de tâches.

Imports :
- 'os' : Module du système d'exploitation pour les opérations
de fichiers et de chemins.
- 'modules.supprimer_taches.SupprimerTache' : Module pour supprimer des tâches.
- 'modules.gestion_des_taches.GestionnaireTaches' : Module pour
gérer des tâches.

Exemple d'utilisation :
- Initialise un gestionnaire de tâches avec un fichier de données CSV.
- Ajoute des tâches d'exemple et gère les exceptions éventuelles.
"""
import os
from modules.supprimer_taches import SupprimerTache
from modules.gestion_des_taches import GestionnaireTaches


nom_fichier_data = 'data_taches.csv'
dossier_data = os.path.join(os.path.dirname(__file__), 'data')
chemin_fichier_csv = os.path.join(dossier_data, nom_fichier_data)


# Exemple d'utilisation
if __name__ == "__main__":
    try:
        gestionnaire = GestionnaireTaches(chemin_fichier_csv)
        supprimeur = SupprimerTache(gestionnaire)
        gestionnaire.ajouter_tache("tache1", "Description de la tâche 1")
        gestionnaire.ajouter_tache("tache2", "Description de la tâche 2")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
