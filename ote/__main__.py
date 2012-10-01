"""This is the main ote script

Usage:
  ote help [<subcommand>]
  ote lint [path]
  ote test [path]

"""
import sys;

import docopt

from ote import __version__

def main(argv=sys.argv, stdin=sys.stdin, stdout=sys.stdin,
         stderr=sys.stderr):
    """The main entry point"""
    arguments = docopt.docopt(__doc__, argv[1:], version=__version__)
    print arguments
    

if __name__ == '__main__':
    main()
