"""module permettant d'utiliser des tâches relatifs au système"""
import os
import logging
import pandas as pd

# Configure the logging
log_filename = 'tache_logs.log'  # Specify the log file name

logging.basicConfig(
    # Set the desired logging level (e.g., INFO, DEBUG, ERROR)
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to the console
        logging.FileHandler(log_filename)  # Log to a file
    ]
)

# Create a logger for your module
logger = logging.getLogger(__name__)


class Tache:
    """
    Classe pour représenter une tâche.

    Cette classe contient des attributs pour le nom, la description et l'état de la tâche.
    l'etat de la tache est == False par défaut
    """

    def __init__(self, nom, description):
        self.nom = nom
        self.description = description
        self.terminee = False


class GestionnaireTaches:
    """classe permettant d'ajouter et sauvegarder les tâches
    """

    def __init__(self, fichier_csv):
        self.fichier_csv = fichier_csv
        if os.path.isfile(fichier_csv):
            # Si le fichier CSV existe, chargez les données dans self.taches
            self.taches = self.charger_taches()
        else:
            # Si le fichier n'existe pas, initialisez self.taches comme une liste vide
            self.taches = []

    def ajouter_tache(self, nom, description):
        """
        Ajoute une nouvelle tâche à la liste de tâches.

        :param nom: Le nom de la tâche.
        :param description: La description de la tâche.
        :return: Aucune valeur de retour.
        """
        tache = Tache(nom, description)
        self.taches.append(tache)
        self.sauvegarder_taches()
        logger.info("Added task: %s", nom)

    def sauvegarder_taches(self):
        """
        Ajoute une nouvelle tâche à la liste de tâches.

        :param nom: Le nom de la tâche.
        :param description: La description de la tâche.
        :return: Aucune valeur de retour.
        """
        donnees = {
            "nom": [tache.nom for tache in self.taches],
            "description": [tache.description for tache in self.taches],
            "terminee": [tache.terminee for tache in self.taches],
        }
        df = pd.DataFrame(donnees)

        # Enregistrez le DataFrame dans le fichier CSV
        df.to_csv(self.fichier_csv, index=False)
        logger.info("Saved tasks to CSV file")

    def charger_taches(self):
        # Chargez les données à partir du fichier CSV dans un DataFrame
        df = pd.read_csv(self.fichier_csv)

        # Créez des instances de la classe Tache à partir des données du DataFrame
        taches = []
        for index, row in df.iterrows():
            tache = Tache(row['nom'], row['description'])
            tache.terminee = row['terminee']
            taches.append(tache)
        logger.info("Loaded tasks from CSV file")
        return taches
