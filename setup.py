#!/usr/bin/env python3
import setuptools
from object_colors import Purge


def readme():
    with open("README.rst", "r") as file:
        return file.read()


setuptools.setup(
    description=(
        "A versatile class for conveniently adding color and effects to "
        "Python scripts"
    ),
    long_description=readme(),
    long_description_content_type="text/x-rst",
    url="https://github.com/jshwi/object_colors",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=["object_colors"],
    packages=setuptools.find_packages(exclude=("tests",)),
    include_package_data=True,
    zip_safe=True,
    install_requires=["pytest"],
    python_requires='>=3.8',
    cmdclass={"purge": Purge}
)
