import subprocess
from subprocess import PIPE

ERROR_TEMPLATE = "Pylint failed to run with error code {0}, stderr: {1})"

def parse_line(line):
	"Parse a line of pylint output"
	#broke.py:1: [C] Missing docstring
	file_string, line_string, more = line.split(':')
	line = int(line_string)
	
	return {'line':line, 'filename':file_string}
	

def lint(args):
	filename = args['filename']
	# IMPROVEMENT: Timeouts?
	# IMPROVEMENT: Using the version of path (VIRTUALENV?)
	# IMPROVEMENT: warnings and errors should be distinguished
	# IMPROVEMENT: recognizing when pylint errors out
	p = subprocess.Popen(['pylint', '-E', '--output-format=parseable', filename], 
		stdout=PIPE, stderr=PIPE)
	output, err = p.communicate()
	
	for line in err.splitlines():
		if line.startswith('No config file'):
			continue
		else:
			raise Exception('pylint failed {0}'.format(err))
	
	# IMPROVEMENT: Parsing of pylint errors codes
	lintResult = []

	print output.splitlines()
	for line in output.splitlines():
		lintResult.append(parse_line(line))		
	
	return {'errors': lintResult}
	
