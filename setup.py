#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

#exec(open("xee/version.py").read())
__version__ = "3.0.3"

setup(
    name='xee',
    version=__version__,
    packages=find_packages(),
    author='quentin7b',
    description='SDK for Xee APIs (https://dev.xee.com)',
    long_description=open('README.md').read(),
    install_requires=[
        'isodate',
        'requests'
    ],
    include_package_data=True,
    url='https://github.com/Hector47/xee-sdk-python',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
