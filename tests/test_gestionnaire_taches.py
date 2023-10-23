
import unittest
from modules.gestion_des_taches import GestionnaireTaches
from modules.supprimer_taches import SupprimerTache


class TestGestionnaireTaches(unittest.TestCase):
    def test_ajouter_tache(self):
        gestionnaire = GestionnaireTaches('tests/test_data.csv')
        gestionnaire.ajouter_tache("Tâche 1", "Description de la tâche 1")
        gestionnaire.ajouter_tache("Tâche 2", "Description de la tâche 2")
        self.assertEqual(len(gestionnaire.taches), 2)

    def test_sauvegarder_taches(self):
        # Écrivez un test pour la méthode sauvegarder_taches
        # Assurez-vous qu'elle enregistre correctement les tâches dans un fichier CSV
        pass


class TestSupprimerTaches(unittest.TestCase):
    def test_supprimer_tache(self):
        gestionnaire = GestionnaireTaches('tests/test_data.csv')
        supprimeur = SupprimerTache(gestionnaire)
        supprimeur.supprimer_tache("Tâche 1")
        supprimeur.supprimer_tache("Tâche 2")
        self.assertEqual(len(gestionnaire.taches), 0)


if __name__ == '__main__':
    unittest.main()
