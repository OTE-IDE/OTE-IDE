"""Tests for the ote command"""
from StringIO import StringIO

import mock

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


def test_test_command_should_load_config():
    """ote test should call ote.test.run with arguments"""
    # Arrange

    # Act
    with mock.patch('ote.config.load', return_value={}) as test:
        exit_code, stdout, stderr = run_command(['test'])
        
    # Assert
    assert test.called_once_with(None)


def test_test_command_should_pass_path_to_config_load():
    """ote test should call ote.test.run with arguments"""
    # Arrange

    # Act
    with mock.patch('ote.config.load', return_value={}) as test:
        exit_code, stdout, stderr = run_command(['test', 'a path'])
        
    # Assert
    assert test.called_once_with('a path')
    

def test_test_command_should_return_failure_if_no_test_plugin_configured():
    """ote test should fail if there is no test plugin in the configuration
    """
    with mock.patch('ote.config.load', return_value={}):
        exit_code, stdout, stderr = run_command(['test'])

    assert exit_code == 1
    assert "No test runner plugin configured" in stderr


# def test_test_command_should_try_to_load_test_plugin():
#     """ote test should try to load a configured test plugin"""
#     # Arrange
#     config = {'plugins': {'test-runner': 'nose'}}

#     # Act
#     with mock.patch('ote.config.load', return_value=config):
#         with mock.patch('ote.plugins.load') as load:
#             exit_code, stdout, stderr = run_command(['test'])

#     # Assert
#     load.assert_called_once_with('nose')
    
    
    
    
