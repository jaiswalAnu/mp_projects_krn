# from setuptools import find_packages,setup
# from typing import List

# def get_requirements(file_path:str)->List[str]:
#     '''
#     this function will return the list of requirements
#     '''
#     requirements=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace('/n',"") for req in requirements]
#     return requirements







# setup(
#     name='ml_projecys',
#     version='0.0.1',
#     author='anurag',
#     author_email='anuragjaiswal50877@gmail.com',
#     packages=find_packages(),
#     install_requires=get_requirements('requirements.txt')
# )

# code error
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != "-e ."]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ml_projects',  # fixed typo from 'ml_projecys'
    version='0.0.1',
    author='anurag',
    author_email='anuragjaiswal50877@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
