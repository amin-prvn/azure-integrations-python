import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
import os
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="azure-integration",  # Replace with your own username
    version="0.0.2",
    author="Mehran Zolghadr",
    author_email="mehran@keyleadhealth.com",
    description="Microsoft Azure Integration",
    license = "Apache License 2.0",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=setuptools.find_packages(),
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)