"""
Importe les modules et packages nécessaires et fournit un 
exemple d'utilisation.

Imports :
- 'os' : Module du système d'exploitation pour les opérations de fichiers
 et de dossiers.
- 'tkinter as tk' : Module tkinter pour l'interface utilisateur graphique.
- 'modules.gestion_des_taches.GestionnaireTaches' : Module 
pour gérer les tâches.
- 'modules.app_gui.InterfaceUtilisateur' : Module pour l'interface utilisateur.
"""
import os
import tkinter as tk
from modules.gestion_des_taches import GestionnaireTaches
from modules.app_gui import InterfaceUtilisateur

# Chemin du fichier CSV de données des tâches
NOM_FICHIER_DATA = 'data_taches.csv'
dossier_data = os.path.join(os.path.dirname(__file__), 'data')
chemin_fichier_csv = os.path.join(dossier_data, NOM_FICHIER_DATA)

# Exemple d'utilisation
if __name__ == "__main__":
    root = tk.Tk()

    # Calculer la taille de la fenêtre en pourcentage de la taille de l'écran
    largeur_ecran = root.winfo_screenwidth()
    hauteur_ecran = root.winfo_screenheight()
    largeur_fenetre = int(largeur_ecran * 0.7)  # 70% de la largeur de l'écran
    hauteur_fenetre = int(hauteur_ecran * 0.7)  # 70% de la hauteur de l'écran

    # Définir la taille de la fenêtre
    root.geometry(f"{largeur_fenetre}x{hauteur_fenetre}")

    gestionnaire_taches = GestionnaireTaches(chemin_fichier_csv)
    app = InterfaceUtilisateur(root, gestionnaire_taches)

    # Créez un bouton pour quitter l'application
    def quitter():
        """
        Fonction pour quitter l'application.

        """
        root.destroy()
    quitter_bouton = tk.Button(root, text="Quitter", command=quitter)
    quitter_bouton.pack()

    app.afficher_taches()  # Affiche les tâches existantes
    root.mainloop()
