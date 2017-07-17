#!/usr/bin/python3

from distutils.core import setup
# from setuptools import setup

setup(
    name='pigpio',
    version='0.1',
    description='Real-time GPIO control on the Raspberry Pi',
    author='Omer Akram',
    author_email='omer.akram@crossbario.com',
    packages=['pigpio'],
    entry_points={
        'console_scripts': ['pigpio = pigpio.runner:main']
    },
)
