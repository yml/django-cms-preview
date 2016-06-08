#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='preview',
    version='1.0',
    description="",
    author="Yann Malet",
    author_email='yann.malet@gmail.com',
    url='',
    packages=find_packages(),
    package_data={'preview': ['static/*.*', 'templates/*.*']},
    scripts=[],
)
