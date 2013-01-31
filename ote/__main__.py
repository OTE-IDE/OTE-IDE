"""This is the main ote script

Usage:
  ote help [<subcommand>]
  ote lint [<path>]
  ote test [<path>]

"""
import sys

import docopt

from ote import __version__
import ote.config
import ote.plugins

def _help(_stdin, stdout, _stderr, **_kwargs):
    print >> stdout, docopt.printable_usage(__doc__)


def _lint(_stdin, stdout, _stderr, **kwargs):
    print >> stdout, "Linting", kwargs.get('<path>', '')


def _test(_stdin, stdout, stderr, **kwargs):
    path = kwargs.get('<path>')
    config = ote.config.load(path)
    plugin_name = config.get('plugins', {}).get('test-runner')
    if plugin_name is None:
        print >> stderr, "No test runner plugin configured"
        return 1
    plugin = ote.plugins.load(plugin_name)
    plugin.run()


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
