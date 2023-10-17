import unittest
from modules.gestion_des_taches import GestionnaireTaches

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

if __name__ == '__main__':
    unittest.main()