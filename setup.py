"""
importer setuptools
"""
from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="To_do_list_app",
    version="1.0.0",
    packages=find_packages(),
    install_requires=requirements,
)
