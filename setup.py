"""The setup and build script for the pyadmitad library."""
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

__author__ = 'trezorg@gmail.com'
__version__ = '0.0.1'

setup(
    name="stack2queue",
    version=__version__,
    author='Igor Nemilentsev',
    author_email='trezorg@gmail.com',
    description='Queue by 2 stack on python',
    license='MIT',
    url='https://github.com/trezorg/stack2queue.git',
    keywords='queue, stack',
    packages=find_packages(exclude='tests'),
    test_suite='unittest2.collector',
    tests_require=['unittest2'],
)

