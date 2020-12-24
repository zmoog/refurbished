# -*- coding: utf-8 -*-
from setuptools import setup, find_packages  # noqa: H301

with open("README.md") as f:
    long_description = f.read()

NAME = "refurbished"
REQUIRES = ["beautifulsoup4 >= 4.9.3", "requests >= 2.25.1", "price-parser == 0.3.4"]

setup(
    name=NAME,
    version="0.2.0",
    description="library to search refurbished products on the Apple Store",
    author_email="maurizio.branca@gmail.com",
    url="https://github.com/zmoog/refurbished",
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
