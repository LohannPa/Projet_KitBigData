"""Module permettant d'utiliser des tâches relatives au système."""
import os
import logging
import pandas as pd


# Configure the logging
LOG_FILENAME = 'tache_logs.log'  # Specify the log file name

logging.basicConfig(
    # Set the desired logging level (e.g., INFO, DEBUG, ERROR)
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to the console
        logging.FileHandler(LOG_FILENAME)  # Log to a file
    ]
)

# Create a logger for your module
logger = logging.getLogger(__name__)


class Tache:
    """
    Classe pour représenter une tâche.

    Contient des attributs: nom, description et état de la tâche.
    L'état de la tâche est False par défaut.
    """

    def __init__(self, nom, description):
        """
        Initialise une instance de la classe Tache.

        :param nom: Le nom de la tâche.
        :param description: La description de la tâche.
        """
        self.nom = nom
        self.description = description
        self.terminee = False


class GestionnaireTaches:
    """
    Classe permettant d'ajouter et sauvegarder les tâches.
    """

    def __init__(self, fichier_csv):
        """
        Initialise une instance de la classe GestionnaireTaches.

        :param fichier_csv: Le nom du fichier CSV pour le stockage des tâches.
        """
        self.fichier_csv = fichier_csv
        if os.path.isfile(fichier_csv):
            # Si le fichier CSV existe, chargez les données dans self.taches
            self.taches = self.charger_taches()
        else:
            # Si le fichier n'existe pas,
            # initialisez self.taches comme une liste vide
            self.taches = []

    def ajouter_tache(self, nom, description):
        """
        Ajoute une nouvelle tâche à la liste de tâches.

        :param nom: Le nom de la tâche.
        :param description: La description de la tâche.
        :return: Aucune valeur de retour.
        """
        try:
            tache = Tache(nom, description)
            self.taches.append(tache)
            self.sauvegarder_taches()
            logger.info("Added task: %s", nom)
        except Exception as e:
            logger.error("Erreur lors de l'ajout de la tâche: %s", e)

    def sauvegarder_taches(self):
        """
        Sauvegarde les tâches dans un fichier CSV.

        :return: Aucune valeur de retour.
        """
        try:
            donnees = {
                "nom": [tache.nom for tache in self.taches],
                "description": [tache.description for tache in self.taches],
                "terminee": [tache.terminee for tache in self.taches],
            }
            df = pd.DataFrame(donnees)

            # Enregistrez le DataFrame dans le fichier CSV
            df.to_csv(self.fichier_csv, index=False)
            logger.info("Saved tasks to CSV file")
        except Exception as e:
            logger.error("Erreur lors de la sauvegarde de la tâche: %s", e)

    def charger_taches(self):
        """
        Charge les tâches à partir d'un fichier CSV.

        :return: Une liste d'instances de Tache.
        """
        try:
            # Charger les données à partir du fichier CSV dans un DataFrame
            df = pd.read_csv(self.fichier_csv)

            # Crée des instances de classe Tache à partir du DataFrame
            taches = []
            for index, row in df.iterrows():
                tache = Tache(row['nom'], row['description'])
                tache.terminee = row['terminee']
                taches.append(tache)
            logger.info("Loaded tasks from CSV file")
            return taches
        except Exception as e:
            logger.error("Erreur lors du chargement de la tâche: %s", e)
            donnees = {
                "nom": [tache.nom for tache in self.taches],
                "description": [tache.description for tache in self.taches],
                "terminee": [tache.terminee for tache in self.taches],
            }
        df = pd.DataFrame(donnees)
        # Enregistrez le DataFrame dans le fichier CSV
        df.to_csv(self.fichier_csv, index=False)

    def changer_statut_tache(self, nom):
        """
        Change l'état de la tâche avec le nom donné.

        :param nom: Le nom de la tâche à mettre à jour.
        :return: Aucune valeur de retour.
        """
        for tache in self.taches:
            if tache.nom == nom:
                tache.terminee = not tache.terminee
                self.sauvegarder_taches()

    def supprimer_tache(self, nom):
        """
        Supprime une tâche de la liste.

        :param nom: Le nom de la tâche à supprimer.
        :return: Aucune valeur de retour.
        """
        tache_a_supprimer = None
        for tache in self.taches:
            if tache.nom == nom:
                tache_a_supprimer = tache
                break

        if tache_a_supprimer:
            self.taches.remove(tache_a_supprimer)
            self.sauvegarder_taches()
