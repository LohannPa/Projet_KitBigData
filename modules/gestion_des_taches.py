import os
import pandas as pd


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

    def charger_taches(self):
        # Chargez les données à partir du fichier CSV dans un DataFrame
        df = pd.read_csv(self.fichier_csv)
        
        # Créez des instances de la classe Tache à partir des données du DataFrame
        taches = []
        for index, row in df.iterrows():
            tache = Tache(row['nom'], row['description'])
            tache.terminee = row['terminee']
            taches.append(tache)
        
        return taches
    


