from setuptools import find_packages, setup
from typing import List

# declaring variables for setup functions
PROJECT_NAME='housing-price-prediction'
VERSION='0.0.2'
AUTHOR='Abhishek Pandey'
DESCRIPTION='this is my first end-to-end ml project'
REQUIREMENT_FILE_NAME='requirements.txt'

def get_requirements_list()->List[str]:
    """
    Description: This function reads the requirements.txt file and returns a list of external requirements.
    
    Returns: This function returns a list of external libraries mentioned in the requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name=PROJECT_NAME,
version=VERSION,    
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),                       # custom packages created by the user.
install_requires=get_requirements_list(),        # external packages required by the user.


)