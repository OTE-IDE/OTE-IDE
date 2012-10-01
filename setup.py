from setuptools import setup, find_packages

setup(
    name="OTE-IDE: The One True Editor IDE",
    version="0.1", # TODO: Get from __version__.py
    packages=find_packages(),
    entry_points = {'console_scripts': ['ote = ote.__main__:main']},
    install_requires=['mock', 'nose', 'docopt'],
)    

