from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","").strip() for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='completemlproject',
    version='0.0.1',
    author='Ansto',
    author_email='anstochibamu@gmail.com',
    package_dir={"": "src"},  # Add this line to specify src directory
    packages=find_packages(where="src"),  # Modify this line
    install_requires=get_requirements('requirements.txt')
)