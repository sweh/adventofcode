""" """
from setuptools import find_packages, setup

setup(
    name="session",
    version="0.1.0.dev0",
    install_requires=[
        "requests",
    ],
    author="",
    author_email="",
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ),
    packages=find_packages("src"),
    package_dir={"": "src"},
)
