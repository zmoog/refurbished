# -*- coding: utf-8 -*-
from setuptools import setup, find_packages  # noqa: H301

with open("README.md") as f:
    long_description = f.read()

NAME = "refurbished"
VERSION = "0.7.1"
REQUIRES = [
    "beautifulsoup4 >= 4.9.3",
    "requests >= 2.25.1",
    "price-parser >= 0.3.3",
    "click >= 7.1.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Library to search refurbished products on the Apple Store",
    author="Maurizio Branca",
    author_email="maurizio.branca@gmail.com",
    url="https://github.com/zmoog/refurbished",
    scripts=['cli/rfrb'],
    keywords=[],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    classifiers=[  # https://pypi.org/classifiers/
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
)
