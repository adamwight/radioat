#!/usr/bin/env python3
import os.path
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="radioat",
    version="0.2",
    packages=["radioat"],
    author="Adam Wight",
    author_email="adamw@ludd.net",
    description="Record Internet radio on a crontab",
    long_description=read('README.md'),
    license="GPLv3.0",
    url="https://github.com/adamwight/radioat",
    entry_points={
        "console_scripts": [
            "record_now = radioat.record_now:main",
            "schedule = radioat.schedule:main",
        ],
    },
    install_requires=[
        "docopt",
        "python-crontab",
        "requests"
    ]
)
