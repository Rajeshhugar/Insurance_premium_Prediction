from setuptools import find_packages, setup
from typing import List

requriment_file_name = "requirements.txt"
REMOVE_PACKAGE = "-e ."

def get_requirements()->List[str]:
    with open(requriment_file_name) as requirement_file:
        requriment_list = requirement_file.readline()
    requriment_list = [requirement_name.replace("\n", "") for requirement_name in requriment_list]

    if REMOVE_PACKAGE in requriment_list:
        requriment_list.remove(REMOVE_PACKAGE)
    return requriment_list



setup(name='Insurance',
    version='0.0.1',
    description='Insurance Premium Prediction',
    author='Rajesh Hugar',
    author_email='rajeshhugar94@gmail.com',
    packages=find_packages(),
    install_reqires = get_requirements()
     )