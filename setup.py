#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='markeast',
    packages=['markeast'],
    version='0.1',
    description='Markdown to HTML-rendered Markdown converter',
    long_description=long_description,
    author='Tobias Kienzler',
    author_email='zommuter@gmail.com',
    url='https://github.com/zommuter/markeast',
    license='GPL',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Text Editors :: Text Processing',
        'Topic :: Text Processing :: Markup',
    ],
    install_requires=[],
)
