#!/bin/bash
echo "Exécution des tests..."
python3 -m unittest discover tests
read -p "Appuyez sur Entrée pour continuer..."
