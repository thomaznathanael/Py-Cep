
# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages

with open('README.md') as read_me:
    long_description = read_me.read()
    
import pycep

version = pycep.__version__

install_requires = [
    'requests>=2.9.1'
]

setup(
    name='Py-Cep',
    version=version,
    author='Thomaz Nathanael',
    author_email='thomaznathanael@gmail.com',
    scripts=['exemplo.py', 'README.md'],
    url='https://github.com/thomaznathanael/Py-Cep',
    license='LICENSE',
    description="Um simples modulo para obter informacoes de um CEP",
    long_description=long_description,
    install_requires=install_requires,
    platforms = 'any',
    long_description_content_type='text/markdown',
    keywords=['cep', 'json', 'api', 'pycep', 'py-cep'],
    packages=find_packages(),
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],	
)
