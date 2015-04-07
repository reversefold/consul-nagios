#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='consul-nagios',
    version='0.1.0',
    description='Convert Consul health checks back into nagios plugin compliant exit codes and output.',
    author='Justin Patrin',
    author_email='papercrane@reversefold.com',
    url='https://github.com/reversefold/consul-nagios',
    packages=find_packages(),
    license='MIT',
    install_requires=[
        'docopt>=06.2',
        'python-consul>=0.3.15',
    ],
)
