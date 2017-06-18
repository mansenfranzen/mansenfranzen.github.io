"""This module contains convenience functions"""

import os
import errno


def make_sure_path_exists(path):
    """Credit goes to
    https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
    """
    path = os.path.dirname(path)

    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise