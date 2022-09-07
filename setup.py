from setuptools import setup
from typing import List

# Declare variables for the setup function
PROJECT_NAME = "Housing Predictor"
VERSION = "0.0.1"
AUTHOR = "Eric Tran"
DESCRIPTION = "This is an End-to-end Machine Learning Project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return the list of requirement mention in requirements.txt
    Return: List of required libraries in requirements.txt
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_files:
        return requirement_files.readlines()

setup (
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = PACKAGES,
    install_requires = get_requirements_list(),
)

# if __name__ == "__main__":
#     print(get_requirements_list())