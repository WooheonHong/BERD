# setup.py
import io
from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# Read in the README for the long description on PyPI
def long_description():
    with io.open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
    return readme


setup(
    name="BERD",
    version="0.1",
    description="Show biomedical entity network",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/WooheonHong/BERD",
    author="Wooheon Hong/Jaehyun Lee",
    author_email="quasar103@postech.ac.kr",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GPL v2.0",
        "Operating System :: OS Independent",
    ],
    python_requires="==3.7",
    install_requires=requirements,
    zip_safe=False,
)
