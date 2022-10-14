from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing",
    version="0.0.1",
    author="José Augusto",
    author_email="my_email",
    description="Test version - Image processing. This package is a demo for simulation of upload on the Test Pypi website.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaugustorc/Criacao-de-pacotes-em-Python.git"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)