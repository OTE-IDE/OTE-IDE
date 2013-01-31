import os
import os.path

import configobj

from ote import constants
import ote.utils


def load_config(project_root=None):
    """Return a dictionary of configuration

    if project_root is not provided, it will be looked up from the
    current working directory.
    """
    if project_root is None:
        project_root = ote.utils.find_project_root()

    config_path = os.path.join(project_root,
                               constants.OTE_PROJECT_FILENAME)

    return configobj.ConfigObj(config_path,
                               encoding=constants.CONFIG_FILE_ENCODING)


# Alias as config.load_config isn't as nice as config.load()
load = load_config
