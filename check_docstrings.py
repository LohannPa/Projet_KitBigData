import sys
import os
import glob
from pydocstyle import check

# Use the GITHUB_WORKSPACE environment variable
# to get the root directory of the repository
repository_root = os.environ.get('GITHUB_WORKSPACE', '.')

# You can define a directory or pattern for Python files within the repository
python_files_pattern = os.path.join(repository_root, '*.py')
python_files = glob.glob(python_files_pattern)

# Run docstring checks on the specified directory
exit_code = check(python_files)
sys.exit(exit_code)
