#!/bin/bash
echo "Exécution des tests..."
python -m unittest tests.test_gestionnaire_taches.TestGestionnaireTaches.test_ajouter_tache
read -p "Appuyez sur Entrée pour continuer les tests..."
python -m unittest tests.test_gestionnaire_taches.TestSupprimerTaches.test_supprimer_tache
read -p "Appuyez sur Entrée pour continuer..."
