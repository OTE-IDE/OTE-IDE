"""Common utilities for ote"""

import os
import os.path

OTE_PROJECT_FILENAME = '.ote-project'


class NoProjectException(Exception):

    def __init__(self, path):
        super(NoProjectException, self).__init__(path)
        self.path = path


def find_project_root(start_path=None):
    """Return the path to the project root

    This walks up the filesystem looking for a .ote-project file.
    """
    start_path = os.getcwd() if start_path is None else start_path
    path = start_path
    
    while path:
        if OTE_PROJECT_FILENAME in os.listdir(path):
            break
        head, tail = os.path.split(path)
        if not tail: # Signifies no separators in path
            raise NoProjectException(start_path)
        path = head
    return path
    
    
    
