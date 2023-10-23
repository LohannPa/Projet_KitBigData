
import unittest
from modules.gestion_des_taches import GestionnaireTaches
from unittest.mock import Mock
import csv
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

    def test_modifier_statut(self):
        mocked_function = Mock(
            return_value=[
                ['nom', 'description', 'terminee'],
                ['Tâche 1', 'Description de la tâche 1', 'False'],
                ['Tâche 2', 'Description de la tâche 2', 'False'],
                ['Tâche 2', 'Description de la tâche 2', 'False'],
                ['Tâche 2', 'Description de la tâche 2', 'True'],
                ['Tâche 3', 'Description de la tâche 3', 'True']
            ]
        )
        test_data = mocked_function()

        with open('tests/modifier_statut_test_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for row in test_data:
                writer.writerow(row)

        gestionnaire = GestionnaireTaches(
            'tests/modifier_statut_test_data.csv')
        gestionnaire.modifier_statut('Tâche 1')
        self.assertTrue(gestionnaire.taches[0].terminee)

        gestionnaire.modifier_statut('Tâche 2')
        self.assertTrue(gestionnaire.taches[1].terminee)
        self.assertTrue(gestionnaire.taches[2].terminee)
        self.assertFalse(gestionnaire.taches[3].terminee)

        gestionnaire.modifier_statut('Tâche 3')
        self.assertFalse(gestionnaire.taches[4].terminee)


class TestSupprimerTaches(unittest.TestCase):
    def test_supprimer_tache(self):
        gestionnaire = GestionnaireTaches('tests/test_data.csv')
        supprimeur = SupprimerTache(gestionnaire)
        supprimeur.supprimer_tache("Tâche 1")
        supprimeur.supprimer_tache("Tâche 2")
        self.assertEqual(len(gestionnaire.taches), 0)


if __name__ == '__main__':
    unittest.main()
