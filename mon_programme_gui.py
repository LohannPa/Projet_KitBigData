import os
import tkinter as tk
from modules.gestion_des_taches import GestionnaireTaches
from modules.app_gui import InterfaceUtilisateur

# Chemin du fichier CSV de données des tâches
nom_fichier_data = 'data_taches.csv'
dossier_data = os.path.join(os.path.dirname(__file__), 'data')
chemin_fichier_csv = os.path.join(dossier_data, nom_fichier_data)

# Fonction pour quitter l'application
def quitter():
    root.destroy()

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
    quitter_bouton = tk.Button(root, text="Quitter", command=quitter)
    quitter_bouton.pack()

    app.afficher_taches()  # Affiche les tâches existantes
    root.mainloop()
