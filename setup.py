'''
the setup.py file is an essential part of packaging and distributing 
python projects. it is used by setuptools(or distutils in older python version ) a popular library for packaging python projects, to define
the configuration of your project such as its metadata , dependencies and other information needed to build and distribute the package.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements mentioned in the requirements.txt file
    '''
    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as f:
            #read line from the file 
            lines = f.readlines()
            #process each line 
            for line in lines:
                requirement=line.strip()
                #igrore empty lines and comments -e.
                if requirement and requirement!="-e.":
                    requirements_lst.append(requirement)
            
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")

    return requirements_lst


print(get_requirements('requirements.txt'))

    # with open('requirements.txt','r') as f:
    #     requirements = f.readlines()
    #     requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-r')]
    # return requirements 

setup(
    name='NetworkSecurity',
    version='0.1',
    author="Vaibhav Rathod",
    author_email="vaibhavrathod278@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'))