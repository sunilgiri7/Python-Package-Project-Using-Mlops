from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.4"
PKG_NAME = "Mongo-Connect"
AUTHOR_USERNAME = "sunilgiri"
AUTHOR_EMAIL = "seungiri841@gmail.com"

# Read requirements from requirements_dev.txt
with open("requirements_dev.txt", "r") as f:
    install_requires = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting to a database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sunilgiri7/your-correct-repo-name",
    project_urls={"Bug Tracker": "https://github.com/sunilgiri7/your-correct-repo-name/issues"},
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
