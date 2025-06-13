from setuptools import setup, find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)    
    return requirements

setup(
    name="Fault Detection",
    version="0.0.1",
    author="Ashish Kumar Dubey",
    author_email="dewedi197@gmail.com",
    install_requires=get_requirements("requirements.txt"),  # Fixed
    packages=find_packages(),
)