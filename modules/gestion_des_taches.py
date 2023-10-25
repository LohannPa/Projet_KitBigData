import os
import pandas as pd
import csv


class Tache:
    """
    Classe pour représenter une tâche
    Contient des attributs: nom, description et état de la tâche
    l'etat de la tache == False par défaut
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
        # Charger les données à partir du fichier CSV dans un DataFrame
        df = pd.read_csv(self.fichier_csv)
        # Créer des instances de classe Tache à partir du DataFrame
        taches = []
        for index, row in df.iterrows():
            tache = Tache(row['nom'], row['description'])
            tache.terminee = row['terminee']
            taches.append(tache)
        return taches

    def modifier_statut(self, nom: str):
        """
        Modifie le statut terminee d'une taches designee:
            1. de l'instance cree par la classe GestionnaireTaches
            2. du fichier CSV ou les donnees taches sont sauvegardees

        Args:
            nom (str): Le nom de la tâche.

        Returns:
            Aucun return.
            Modifie directement le statut terminee des taches.
        """

        # Modification de l'objet taches
        for tache in self.taches:
            if tache.nom == nom and tache.terminee is False:
                tache.terminee = True
            elif tache.nom == nom and tache.terminee is True:
                tache.terminee = False

        # Modifier le statut et garder les donnees dans la liste rows
        rows = []
        with open(self.fichier_csv, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row[0] == nom and row[2] == 'False':
                    row[2] = 'True'
                elif row[0] == nom and row[2] == 'True':
                    row[2] = 'False'
                rows.append(row)
            print(rows)

        # Ecrire la liste rows au fichier csv
        with open(self.fichier_csv, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(rows)
