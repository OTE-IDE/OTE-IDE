"""Tests for the ote command"""
from StringIO import StringIO


from ote.__main__ import main

def run_command(args=None, stdin=None):
    """Runs the ote command and returns exitcode, stdout, stderr

    args is any command line arguments
    stdin is any text that should be provided on stdin.
    """
    argv = ['ote'] + (args if args is not None else [])
    stdin = StringIO() if stdin is None else StringIO(stdin)
    stdout, stderr = StringIO(), StringIO()
    exit_code = 0

    try:
        exit_code = main(argv, stdin, stdout, stderr)
    except SystemExit as exc:
        if exc.code is not None:
            stderr.write(exc.code)
            stderr.write('\n')
            exit_code = 1

    return exit_code, stdout.getvalue(), stderr.getvalue()
    

def test_raw_command():
    """ote on its own should display a usage message on standard error"""
    # Arrange

    # Act
    exit_code, stdout, stderr = run_command()

    # Assert
    assert exit_code == 1
    assert "Usage:" in stderr
    assert "ote help [<subcommand>]" in stderr


def test_help_command():
    """ote help should display a usage message on the standard output"""
    # Arrange

    # Act
    exit_code, stdout, stderr = run_command(['help'])

    # Assert
    assert exit_code == 0
    assert "Usage:" in stdout
    assert "ote help [<subcommand>]" in stdout
    

def test_lint_command_with_filename():
	# Arrange
	
	# Act
	exit_code, stdout, stderr = run_command(['lint', 'testdata/errors'])
	
	# Assert
	assert exit_code == 0
	assert ''
	
	
def test_lint_command_without_filename():
	raise Exception('Not implemented')
