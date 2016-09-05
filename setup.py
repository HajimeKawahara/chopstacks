#!/usr/bin/env python


try:
    from setuptools import setup, Extension
    setup, Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
    setup, Extension

import os
import re
import sys

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

vre = re.compile("__version__ = \"(.*?)\"")
m = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "chopstacks.py")).read()

version="0.01"

setup(
    name="chopstacks",
    version=version,
    description="",
    long_description=open("README.md").read(),
    author="Hajime Kawahara",
    author_email="kawahara@eps.u-tokyo.ac.jp",
    url="",
    py_modules=["chopstacks"],
    package_data={"": ["LICENSE"]},
    include_package_data=True,
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    classifiers=[
        "Development Status :: 1",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
