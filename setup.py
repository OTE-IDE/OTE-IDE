from setuptools import setup, find_packages

setup(
    name="OTE-IDE: The One True Editor IDE",
    version="0.1",
    packages=find_packages(),
    entry_points = {'console_scripts': ['ote = ote.__main__:main']},
    install_requires=['mock', 'nose', 'docopt'],
)    

