"""
Contains the utility functions.
"""

import os


def delete_files_in_directory(dir_name: str):
    """
    Remove all the files in the given directory.
    """
    for filename in os.listdir(dir_name):
        os.remove(os.path.join(dir_name, filename))
