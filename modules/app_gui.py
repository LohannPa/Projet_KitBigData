import tkinter as tk
from tkinter import ttk

class InterfaceUtilisateur:
    """
    Classe pour créer une interface utilisateur pour gérer des tâches.
    """

    def __init__(self, root, gestionnaire_taches):
        """
        Initialise une instance de la classe InterfaceUtilisateur.

        :param root: La fenêtre principale de l'interface utilisateur.
        :param gestionnaire_taches: Une instance de GestionnaireTaches.
        """
        self.root = root
        self.gestionnaire_taches = gestionnaire_taches
        self.root.title("Gestionnaire de tâches")

        # Créez un cadre principal pour diviser la fenêtre en trois parties
        cadre_entrees = tk.Frame(root)
        cadre_boutons = tk.Frame(root)
        cadre_affichage = tk.Frame(root)

        cadre_entrees.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        cadre_boutons.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        cadre_affichage.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Créez des entrées pour le nom et la description des tâches
        self.label_nom = tk.Label(cadre_entrees, text="Nom de la tâche:")
        self.label_nom.pack(side=tk.LEFT)
        self.nom_tache = tk.Entry(cadre_entrees)
        self.nom_tache.pack(side=tk.LEFT)

        self.label_description = tk.Label(cadre_entrees, text="Description de la tâche:")
        self.label_description.pack(side=tk.LEFT)
        self.description_tache = tk.Entry(cadre_entrees)
        self.description_tache.pack(side=tk.LEFT)

        # Créez des boutons pour ajouter, supprimer et changer le statut des tâches
        self.ajouter_bouton = tk.Button(cadre_boutons, text="Ajouter une tâche", command=self.ajouter_tache)
        self.ajouter_bouton.pack(side=tk.LEFT)

        self.supprimer_bouton = tk.Button(cadre_boutons, text="Supprimer", command=self.supprimer_tache)
        self.supprimer_bouton.pack(side=tk.LEFT)

        self.changer_statut_bouton = tk.Button(cadre_boutons, text="Changer le statut", command=self.changer_statut_tache)
        self.changer_statut_bouton.pack(side=tk.LEFT)

        # Créez un Treeview pour afficher les tâches sous forme de tableau
        self.tableau_taches = ttk.Treeview(cadre_affichage, columns=("Nom", "Description", "Statut"))
        self.tableau_taches.heading("#1", text="Nom")
        self.tableau_taches.heading("#2", text="Description")
        self.tableau_taches.heading("#3", text="Statut")
        self.tableau_taches.pack(fill=tk.BOTH, expand=True)

    def ajouter_tache(self):
        """
        Ajoute une tâche en utilisant les valeurs des entrées.

        :return: Aucune valeur de retour.
        """
        nom = self.nom_tache.get()
        description = self.description_tache.get()
        if nom and description:
            self.gestionnaire_taches.ajouter_tache(nom, description)
            self.afficher_taches()  # Met à jour le tableau des tâches

    def supprimer_tache(self):
        """
        Supprime les tâches sélectionnées du tableau.

        :return: Aucune valeur de retour.
        """
        selection = self.tableau_taches.selection()
        if selection:
            for item in selection:
                nom_tache = self.tableau_taches.item(item, "values")[0]
                self.gestionnaire_taches.supprimer_tache(nom_tache)
            self.afficher_taches()  # Met à jour le tableau des tâches après la suppression

    def changer_statut_tache(self):
        """
        Change le statut des tâches sélectionnées dans le tableau.

        :return: Aucune valeur de retour.
        """
        selection = self.tableau_taches.selection()
        if selection:
            for item in selection:
                nom_tache = self.tableau_taches.item(item, "values")[0]
                self.gestionnaire_taches.changer_statut_tache(nom_tache)
            self.afficher_taches()  # Met à jour le tableau des tâches après la modification du statut

    def afficher_taches(self):
        """
        Affiche les tâches dans le tableau.

        :return: Aucune valeur de retour.
        """
        for i in self.tableau_taches.get_children():
            self.tableau_taches.delete(i)
        for tache in self.gestionnaire_taches.taches:
            terminee = "Terminée" if tache.terminee else "En cours"
            self.tableau_taches.insert("", "end", values=(tache.nom, tache.description, terminee))
