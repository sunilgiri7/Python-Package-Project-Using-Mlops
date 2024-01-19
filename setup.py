from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e.'

def get_requirement(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.4'
REPO_NAME = "mongodbconnectorpkg"
PKG_NAME = "Mongo-Connect"
AUTHOR_USERNAME = "sunilgiri"
AUTHOR_EMAIL = 'seungiri841@gmail.com'

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting to a database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sunilgiri7/your-correct-repo-name",
    project_urls={
        "Bug Tracker": "https://github.com/sunilgiri7/your-correct-repo-name/issues",
    },
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirement("requirements_dev.txt"),
)
