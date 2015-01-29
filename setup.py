import glob
import os

from setuptools import setup


setup(
    name='Wikipedia Text Extractor',
    scripts=['WikiExtractor.py'],
    description='Wikipedia Text Extractor. Ported to python 3.',
    version='2.6',
    author='Giuseppe Attardi (attardi@di.unipi.it), University of Pisa, Antonio Fuschetto (fuschett@di.unipi.it), University of Pisa',
    author_email='attardi@di.unipi.it',
    url='https://github.com/aesuli/wikipedia-extractor',
    license='GNU General Public License, version 3',
    long_description=open('README.md',encoding='utf8').read(),
)