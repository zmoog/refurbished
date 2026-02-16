# -*- coding: utf-8 -*-
from setuptools import setup, find_packages  # noqa: H301

with open("README.md") as f:
    long_description = f.read()

NAME = "refurbished"

setup(
    name=NAME,
    version="0.12.1",
    description="Library to search refurbished products on the Apple Store",
    author="Maurizio Branca",
    author_email="maurizio.branca@gmail.com",
    url="https://github.com/zmoog/refurbished",
    scripts=['cli/rfrb'],
    keywords=[],
    install_requires=[
        "beautifulsoup4 >= 4.11.1",
        "click ==8.3.1",
        "price-parser == 0.3.4",
        "pydantic >=2.10,<3.0",
        "requests >= 2.28.1",
        "rich >= 12.6.0",        
    ],
    extras_require={
        "test": [
            "pytest==7.2.1",
            "black==22.12.0",
            "isort==5.12.0",
            "flake8==6.1.0",
        ],
    },
    packages=find_packages(exclude=["test", "tests"]),
    python_requires=">=3.10",
    classifiers=[  # https://pypi.org/classifiers/
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
)
