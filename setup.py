#!/usr/bin/env python
# coding: utf-8

from distutils.core import setup

setup(
    name='zsplitjoin',
    version='0.1.0',
    description='Simple split and join files.',
    long_description=open('README.md').read(),
    author='Marcelo Fonseca Tambalo',
    author_email='marcelo.zokis@gmail.com',
    url='https://github.com/zokis/zsplitjoin',
    packages=['zsplitjoin'],
    install_requires=['unipath==1.0'],
    classifiers=(
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3"
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Desktop Environment :: File Managers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    )
)
