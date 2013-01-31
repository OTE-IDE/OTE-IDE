"""Exception heirarchy"""


class OteException(Exception):
    """Base for all exceptions"""


class OteUserError(OteException):
    """Base for all exceptions due to user errors"""


class NoProjectException(OteUserError):
    """Signals that an ote project file could not be found"""

    def __init__(self, path):
        super(NoProjectException, self).__init__(path)
        self.path = path
