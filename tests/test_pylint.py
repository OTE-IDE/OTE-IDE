import sys
sys.path.append('.')

from ote.plugins import pylint_plugin

def errors():
	a = b
	c = 1,1
	

def test_pylint_parser():
	result = pylint_plugin.lint({'filename': __file__}) 
	print result['errors']
	assert result['errors'] == [{'line': 7, 'filename': __file__}]


