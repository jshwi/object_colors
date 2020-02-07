import sys
from configparser import ConfigParser
from os import path, rename, listdir
from shutil import rmtree, which
from subprocess import Popen, PIPE
from typing import Optional

import setuptools

from object_colors import Color


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
        config = ConfigParser()
        config.read("venv.ini")
        if config["DEFAULT"] and config["DEFAULT"]["venv"]:
            return config["DEFAULT"]["venv"]
        return None

    @staticmethod
    def __color_class() -> Color:
        color = Color()
        color.populate_colors()
        return color

    def __clean_repo(self) -> None:
        # list of python artifacts and distribution sources to delete
        # will delete ALL of these items in the repo - recursively
        color = self.__color_class()
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
        for key in files:
            command = f'find . -name {key} -exec rm -rf {{}} + -print'
            key = color.green.bold.get("Executing:")
            val = color.yellow.get(command)
            print(f"{key} {val}")
            with Popen(
                    command,
                    shell=True,
                    stdout=PIPE,
                    bufsize=1,
                    universal_newlines=True
            ) as out:
                for line in out.stdout:
                    print(line, end="")

    @staticmethod
    def __return(exclude: str, up_dir: str) -> None:
        # return the preserved virtual environment to the repo root
        # directory
        if path.isdir(up_dir):
            rename(up_dir, exclude)

    def __resolve_opt(self, exclude: str, up_dir: str) -> None:
        # if choosing to save the virtual environment take it out
        # of the repo root temporarily as removing python cache
        # files from it will render it completely useless
        # otherwise simply delete it
        if path.isdir(exclude):
            if self.ignore:
                rmtree(exclude)
            else:
                rename(exclude, up_dir)

    def __detect_venv(self) -> Optional[str]:
        if hasattr(sys, 'real_prefix'):
            pythonpath = which("python")
            return path.dirname(path.dirname(pythonpath))
        return self.__detect_venv_cfg()

    @staticmethod
    def __detect_venv_cfg() -> Optional[str]:
        repo = listdir(".")
        for item in repo:
            if path.isdir(item):
                files = listdir(item)
                if "pyvenv.cfg" in files:
                    return item
        return None

    @staticmethod
    def __write_config(venv: str):
        config = ConfigParser()
        config["DEFAULT"] = {"venv": venv}
        with open("venv.ini", "w") as file:
            config.write(file)

    def __get_ini(self):
        choice = None
        color = self.__color_class()
        venv = self.__detect_venv()
        if venv:
            color.green.bold.print("Virtual Environment Detected")
            color.yellow.print_key(
                f"{venv} appears to be your current virtual environment.",
                venv
            )
            choice = input(
                color.yellow.get_key(
                    "Is this correct?\n\nY/n] ",
                    "Y/n]",
                    scatter=True
                )
            ).lower()
            if choice == "n":
                venv = None
        if not venv:
            if choice == "n":
                color.red.bold.print("No Virtual Environment Detected")
            venv = input(
                color.yellow.get_key(
                    "Please enter the name of your virtual environment."
                    "\n\n>>>", ">>>", scatter=True

                )
            )
        self.__write_config(venv)
        return venv

    def run(self) -> None:
        if path.isfile("venv.ini"):
            exclude = self.__parse_config()
        else:
            exclude = self.__get_ini()
        up_dir = path.join("..", exclude)
        self.__resolve_opt(exclude, up_dir)
        self.__parse_config()
        self.__clean_repo()
        self.__return(exclude, up_dir)
