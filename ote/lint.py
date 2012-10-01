"""Abstract out interface to a variety of linters
"""
import plugins

def start():
	print 'hi'
	return 'started!'

def lint(linter_name, args):
	"""Lint with linter_name plugin. Return of the form {errors:[{line:, column:,summary:,description:}], version:0} )"""
	# IMPROVEMENT: plugins -> PLUGINS?
	linter = plugins.plugins[linter_name] # maybe do some validation
	return linter.lint(args)



