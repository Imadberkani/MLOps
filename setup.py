from pathlib import Path

from setuptools import find_namespace_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

# Define our package
setup(
    name="model_Columns",
    version=0.1,
    description=" Vertebral column classification",
    author="Imad Berkani et Slimane Tighermet",
    author_email="imad.berkani@insa-rouen.fr",
    url="",
    python_requires=">=3.7",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
)
