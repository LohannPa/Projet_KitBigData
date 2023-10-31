class SupprimerTache:
    """classer permettant de supprimer une tache
    """

    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire

    def supprimer_tache(self, nom_tache):
        """
        Supprime une tâche par son nom.

        :param nom_tache: Le nom de la tâche à supprimer.
        :return: Aucune valeur de retour.
        """
        try:
            self.gestionnaire.taches = [
                tache for tache in self.gestionnaire.taches
                if tache.nom != nom_tache
            ]
            self.gestionnaire.sauvegarder_taches()
        except Exception as e:
            print(f"Erreur lors de la suppression de la tâche : {e}")
