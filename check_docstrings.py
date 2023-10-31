"""
Importe les modules et les paquets nécessaires pour les vérifications
des docstrings.
"""
import sys
import os
import glob
from pydocstyle import check

# Utilise la variable d'environnement GITHUB_WORKSPACE pour obtenir
# le répertoire racine du
# dépôt
repository_root = os.environ.get('GITHUB_WORKSPACE', '.')

# Vous pouvez définir un répertoire ou un motif pour les fichiers Python
# dans le dépôt
python_files_pattern = os.path.join(repository_root, '*.py')
python_files = glob.glob(python_files_pattern)

# Exécute les vérifications des docstrings sur le répertoire spécifié
exit_code = check(python_files)
sys.exit(exit_code)
