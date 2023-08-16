from setuptools import setup
from typing import List  # error fix this

def get_requirements_list()->List[str]:
    '''
    This function is going to return list of requirements mentioned in requirements.txt
    '''
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines()

# declaring a variable for setup function
PROJEC_NAME="Housing predictor"
VERSION= "0.0.1"
AUTHOR="RAMDAS PRAJAPATI"
DESCRIPTION = "THIS IS FIRST FSDS NOV BATCH MACHINE LEARNING PROJECT"
packages = ['housing']
REQUIREMENTS_FILE_NAME = "requirements.txt"


setup(name = PROJEC_NAME,
version = VERSION,
author = AUTHOR,
description = DESCRIPTION,
packages = packages,
install_requires = get_requirements_list(), # or insted find_pakages() so in requirements.txt u have to write e . so that all pakages in current directory get installed
)

if __name__ == "__main__":
    print(get_requirements_list())


