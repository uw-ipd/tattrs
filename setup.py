#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

requirements = [
    "attrs >= 17.3",
]

test_reqs = [
    "numpy",
    "torch >= 0.4",
    "pytest",
]

dev_reqs = [
    "tox",
]

setup(
    name="tattrs",
    version="0.0.1.dev0",
    description="attrs-based tensor classes for numpy and torch",
    long_description=readme,
    author="Alex Ford",
    author_email="fordas@uw.edu",
    url="https://github.com/uw-ipd/tattrs",
    packages=find_packages(where="src", exclude=["tests*"]),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=requirements,
    extras_require={
        "test": test_reqs,
        "dev": test_reqs + dev_reqs,
    },
    license="MIT license",
    zip_safe=False,
    keywords="tattrs",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
