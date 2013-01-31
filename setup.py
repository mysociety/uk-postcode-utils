from distutils.core import setup

setup(
    name='uk-postcode-utils',
    version='0.1.0',
    author='Matthew Somerville',
    author_email='matthew@mysociety.org',
    packages=['ukpostcodeutils', 'ukpostcodeutils.test'],
    url='http://pypi.python.org/pypi/uk-postcode-utils/',
    license='LICENSE.txt',
    description='Functions for handling UK postcodes.',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)