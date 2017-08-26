#!/usr/bin/env python

from distutils.core import setup

setup(name="JSONAutoArray",
    version="0.1",
    description="conveniently write json-serializable python objects to an array in a file",
    author="doug shawhan",
    author_email="doug.shawhan@gmail.com",
    url="neuralpro.be",
    packages=["json_autoarray"],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: ETL",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        ],
    python_requires=">=2.6"
     )
