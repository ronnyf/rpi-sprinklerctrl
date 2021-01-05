from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sprinklerctrl',
    version='0.0.1',
    description='A Sprinkler controller',
    long_description=readme,
    author='Ronny Falk',
    author_email='ronnyf@icloud.com',
    url='https://github.com/ronnyf/rpi-sprinklerctrl',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
