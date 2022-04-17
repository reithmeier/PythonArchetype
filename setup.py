#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="PythonArchetype",
    version="1.0.0",
    description="Empty Python Archetype Project with tox, pylint, black, pytest, coverage",
    author="Lukas Reithmeier",
    license="MIT",
    url="https://github.com/reithmeier/PythonArchetype",
    keywords="python archetype",
    packages=find_packages(where="src"),
    package_dir={"": "src"},  # Optional
)
