#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages
    
setup(
    name="pyCountdownTimer",
    version="1.0",
    url='https://github.com/sys-git/pyCountdownTimer',
    packages=find_packages(),
    package_dir={'pyCountdownTimer': 'pyCountdownTimer'},
    include_package_data=True,
    author="Francis Horsman",
    author_email="francis.horsman@gmail.com",
    description="A count-down timer that periodically checks a flag (to terminate the timer) using a supplied callable.",
    license="GNU General Public License",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications',
    ]
)
