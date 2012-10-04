"""This is the main ote script

Usage:
  ote help [<subcommand>]
  ote lint [<path>]
  ote test [<path>]

"""
import sys
import os

import docopt

from ote import __version__
import ote.config


def _help(stdin, stdout, stderr, **kwargs):
    print >> stdout, docopt.printable_usage(__doc__)


def _lint(stdin, stdout, stderr, **kwargs):
    print >> stdout, "Linting", kwargs.get('<path>', '')


def _test(stdin, stdout, stderr, **kwargs):
    path = kwargs.get('<path>')
    config = ote.config.load(path)
    if 'test-runner' not in config.get('plugins', {}):
        print >> stderr, "No test runner plugin configured"
        return 1
    

SUBCOMMANDS = {
    'help': _help,
    'lint': _lint,
    'test': _test,
}


def main(argv=sys.argv, stdin=sys.stdin, stdout=sys.stdout,
         stderr=sys.stderr):
    """The main entry point"""
    arguments = docopt.docopt(__doc__, argv[1:], version=__version__)
    selected_subcommand, = (key for key, value in arguments.iteritems()
                            if value is True and not key.startswith('<'))
    subcommand = SUBCOMMANDS[selected_subcommand]
    return subcommand(stdin, stdout, stderr, **arguments) or 0


if __name__ == '__main__':
    main()
