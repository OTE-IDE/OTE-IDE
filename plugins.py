import os, sys

sys.path.insert(0, 'plugins')

def load_plugin(name):
	if '.pyc' not in name:
		filename = name.replace('.py','')
		if '.' in filename:
			raise Exception("Invalid Plugin Filename")
		mod = __import__(filename)
		print name + ' returns:' + mod.start()
		return mod

pluginList = os.listdir('plugins')

plugins = {}

for plugin in pluginList:
	plugins[plugin] = load_plugin(plugin)
