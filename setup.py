from __future__ import absolute_import, print_function

from setuptools import setup
import os


# From numpy-stubs/setup.py
def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, '', 1)
            stubs.append(path)
    return {package: stubs}


setup(
    name="boltons-stubs",
	description="PEP 561 type stubs for boltons",
    author="Wil Cooley",
    author_email="wcooley@nakedape.cc",
    url="https://github.com/wcooley/python-boltons-stubs",
    version="18.0.1.0",
    package_data=find_stubs("boltons-stubs"),
    packages=["boltons-stubs"],
    install_requires=[
        "boltons==18.0.1",
    ],
)
