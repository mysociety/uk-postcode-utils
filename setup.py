from setuptools import setup

setup(
    name='uk-postcode-utils',
    version='1.0',
    author='Matthew Somerville',
    author_email='matthew@mysociety.org',
    packages=['ukpostcodeutils', 'ukpostcodeutils.test'],
    url='https://pypi.python.org/pypi/uk-postcode-utils/',
    license='LICENSE.txt',
    description='Functions for handling UK postcodes.',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: GIS',
    ],

)
