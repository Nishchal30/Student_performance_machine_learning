from setuptools import find_packages, setup
from typing import List


def get_requirements(filepath: str) -> List[str]:

    '''this function is created to get the requirements file from file path and return the packages as a list'''
    
    requirements = []

    with open(filepath) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name = "Machine Learning Project",
    version = "1.0.0",
    author = "Nishchal Jinturkar",
    author_email = "nishchaljinturkar30@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)