#!/usr/bin/env python

from setuptools import setup

setup(name="JSONAutoArray",
    version="0.6",
    description="Write self-closing array to JSON file",
    long_description="conveniently write json-serializable python objects to an array in a file",
    author="pathetiq kphretiq",
    author_email="kphretiq@gmail.com",
    maintainer="pathetiq kphretiq",
    maintainer_email="kphretiq@gmail.com",
    url="https://github.com/kphretiq/json-autoarray",
    download_url="https://github.com/kphretiq/json-autoarray",
    packages=["json_autoarray"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        ]
     )
