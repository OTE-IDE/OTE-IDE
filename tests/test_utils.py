"""Tests for the ote.utils module"""

import mock
from nose.tools import assert_raises

from ote.exceptions import NoProjectException
from ote.utils import find_project_root


def test_find_project_root_in_root():
    """
    If we are in the root of a project find_project_root should return path
    """
    # Arrange
    dir_contents = ['setup.py', '.ote-project', '.ote-local', 'src']

    # Act
    with mock.patch('os.listdir', return_value=dir_contents) as listdir:
         root = find_project_root('/home/user/work/proj')

    # Assert
    assert root == '/home/user/work/proj'
    listdir.assert_called_once_with('/home/user/work/proj')

def test_find_project_root_above():
    """
    If there is a .ote-project file above us, find_project_root should return ..
    """
    # Arrange
    dir_contents = iter(
        [['__init__.py', 'module.py', 'test_module.py'],
         ['setup.py', '.ote-project', '.ote-local', 'src']])

    
    # Act
    with mock.patch('os.listdir', side_effect=dir_contents) as listdir:
         root = find_project_root('/home/user/work/proj/src')

    # Assert
    assert root == '/home/user/work/proj'
    assert listdir.mock_calls == [mock.call('/home/user/work/proj/src'), 
                                  mock.call('/home/user/work/proj')]
    
def test_find_project_root_not_present():
    """If there is no .ote-project file, NoProjectException should be raised"""
    # Arrange
    dir_contents = iter(
        [['__init__.py', 'module.py', 'test_module.py'],
         ['setup.py', 'src'],
         ['proj']])

    # Act
    with mock.patch('os.listdir', side_effect=dir_contents) as listdir:
        with assert_raises(NoProjectException) as cm:
            root = find_project_root('/proj/src')

    # Assert
    assert listdir.mock_calls == [mock.call('/proj/src'),
                                  mock.call('/proj'),
                                  mock.call('/')]
    assert cm.exception.path == '/proj/src'

def test_find_project_defaults_to_cwd():
    """
    If no path is provided find_project should default to the working dir
    """
    # Arrange
    patch_getcwd = mock.patch('os.getcwd', return_value='/hello/world')
    patch_listdir = mock.patch('os.listdir', return_value=[])

    # Act
    with patch_getcwd, patch_listdir:
        try:
            find_project_root()
        except NoProjectException as exc:
            pass
    
    # Assert
    assert exc.path == '/hello/world'
