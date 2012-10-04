"""Common utilities for ote"""

import os
import os.path

import logging

import ote.constants
from ote.exceptions import NoProjectException

_log = logging.getLogger(__name__)




def find_project_root(start_path=None):
    """Return the path to the project root

    This walks up the filesystem looking for a .ote-project file.
    """
    _log.debug("Searching for project root for %s", start_path)
    
    start_path = os.getcwd() if start_path is None else start_path

    if os.path.isfile(start_path):
        path = os.path.dirname(start_path)
    else:
        path = start_path
    
    while ote.constants.OTE_PROJECT_FILENAME not in os.listdir(path):
        head, tail = os.path.split(path)
        if not tail: # Signifies no separators in path
            _log.debug("Search for project root failed.  Reached %s",
                       head)
            raise NoProjectException(start_path)
        path = head
    return path
