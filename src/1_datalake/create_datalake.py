"""CREA EL DATA LAKE Y SU ESTRUCTURA"""
"""Create a datalake in the main directory"""

import os
import pkg_resources
from importlib_resources import files, is_resource



STRUCTURE_FILE = "datalake_structure.txt"


def get_datalake_dirs():
    """Returns the datalake directories stored in the file structure.txt"""

    if not pkg_resources.resource_exists(__name__, STRUCTURE_FILE):
        raise FileNotFoundError(f"File {STRUCTURE_FILE} not found")

    with pkg_resources.resource_stream(__name__, STRUCTURE_FILE) as f:
        dirs = f.readlines()
        dirs = [dir.strip() for dir in dirs]
    #if not is_resource('',STRUCTURE_FILE):
    #   raise FileNotFoundError(f"File {STRUCTURE_FILE} not found")
    #else:
    #    print(f"!!!EXISTE: {STRUCTURE_FILE}!!!")

    #filepath=files('README.md').joinpath(STRUCTURE_FILE)
    #with filepath.open('r') as f:
    #    dirs = f.readlines()
    #    dirs = [dir.strip() for dir in dirs]
    #    print(dirs)

    return dirs


def create_datalake(dirs):
    """Creates datalake in the main directory.

    Args:
        dirs (list): List of directories to create

    Return:
        None

    """

    for path in dirs:
        if not os.path.exists(path):
            os.makedirs(path)


def main():
    """Orchestrates the creation of the datalake"""

    dirs = get_datalake_dirs()
    create_datalake(dirs)


if __name__ == "__main__":
    main()
