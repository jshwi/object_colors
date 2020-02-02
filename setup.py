import configparser
import os
import shutil
import subprocess
from typing import Optional
from object_colors import Color

import setuptools


def readme():
    with open("README.rst", "r") as file:
        return file.read()


class Purge(setuptools.Command):
    """Delete ALL python artifacts"""

    user_options = [("ignore=", "i", "keep entered files and dirs")]

    # noinspection PyAttributeOutsideInit
    def initialize_options(self):
        """Abstract method that is required to be overwritten"""
        self.ignore = None

    def finalize_options(self):
        """Abstract method that is required to be overwritten"""

    @staticmethod
    def __parse_config() -> Optional[str]:
        # to use python setup.py purge without deleting virtual
        # environment add:
        #
        # [DEFAULT]
        # venv=<virtual environment>
        #
        # to a config file called `venv.ini`
        config = configparser.ConfigParser()
        config.read("venv.ini")
        if config["DEFAULT"] and config["DEFAULT"]["venv"]:
            return config["DEFAULT"]["venv"]
        return None

    @staticmethod
    def __clean_repo() -> None:
        # list of python artifacts and distribution sources to delete
        # will delete ALL of these items in the repo - recursively
        files = [
            '"build"',
            '"dist"',
            '"__pycache__"',
            '"pip-wheel-metadata"',
            '"htmlcov"',
            '".coverage"',
            '"*.pyc"',
            '"*.egg*"',
            '"*.pyo"',
            '"*~"',
        ]
        color = Color()
        color.populate_colors()
        for key in files:
            command = f'find . -name {key} -exec rm -rf {{}} + -print'
            key = color.green.bold.get("Executing:")
            val = color.yellow.get(command)
            print(f"{key} {val}")
            with subprocess.Popen(
                    command,
                    shell=True,
                    stdout=subprocess.PIPE,
                    bufsize=1,
                    universal_newlines=True
            ) as out:
                for line in out.stdout:
                    print(line, end="")

    @staticmethod
    def __return(exclude: str, up_dir: str) -> None:
        # return the preserved virtual environment to the repo root
        # directory
        if os.path.isdir(up_dir):
            os.rename(up_dir, exclude)

    def __resolve_opt(self, exclude: str, up_dir: str) -> None:
        # if choosing to save the virtual environment take it out
        # of the repo root temporarily as removing python cache
        # files from it will render it completely useless
        # otherwise simply delete it
        if os.path.isdir(exclude):
            if self.ignore:
                shutil.rmtree(exclude)
            else:
                os.rename(exclude, up_dir)

    def run(self) -> None:
        """Parse virtual environment name from config file
        Opt will toggle whether to delete virtual environment or not
        """
        exclude = self.__parse_config()
        up_dir = os.path.join("..", exclude)
        self.__resolve_opt(exclude, up_dir)
        self.__parse_config()
        self.__clean_repo()
        self.__return(exclude, up_dir)


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
