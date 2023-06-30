from setuptools import find_packages,setup
from typing import List

#------------------------------------------------------------
# this function will returns of requirements.txt
#------------------------------------------------------------
def get_requirements()->List[str]:
    requirement_list:List[str] = []
    return requirement_list


     



setup(
    name="sensor",
    version=0.01,
    author="sudheer",
    author_email="sudheer.read@gmail.com",
    long_description="this is sensor project",
    packages=find_packages(),
    install_requires =get_requirements()#["pymongo==4.4.0"],
)

