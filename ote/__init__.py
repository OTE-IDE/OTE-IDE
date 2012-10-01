"""This is the main ote script
Editors will init OTE for the first time with a command through this.
Running a server from this will come later.

Usage:
  ote help [<subcommand>]
  ote lint [<path>]
  ote test [<path>]

"""
import sys;

import docopt

from ote import __version__


def help_(stdin, stdout, stderr, **kwargs):
    print >> stdout, docopt.printable_usage(__doc__)


def lint(stdin, stdout, stderr, **kwargs):
    print >> stdout, "Linting", kwargs.get('<path>', '')


SUBCOMMANDS = {
    'help': help_,
    'lint': lint
}


def main(argv=sys.argv, stdin=sys.stdin, stdout=sys.stdout,
         stderr=sys.stderr):
    """The main entry point"""
    arguments = docopt.docopt(__doc__, argv[1:], version=__version__)
    selected_subcommand, = (key for key, value in arguments.iteritems()
                            if value is True and not key.startswith('<'))
    subcommand = SUBCOMMANDS[selected_subcommand]
    subcommand(stdin, stdout, stderr, **arguments)
    return 0


if __name__ == '__main__':
    main()
