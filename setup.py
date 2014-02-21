#!/usr/bin/env python2
from distutils.core import setup


with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='asstosrt',
    version='0.1.0',
    description='A tool that convert ASS/SSA subtitle to SRT format',
    author='XiErCh',
    author_email='orz@sorz.org',
    url='https://github.com/bluen/asstosrt/',
    py_modules=['asstosrt', '_shell_helper'],
    entry_points="""
    [console_scripts]
    asstosrt = asstosrt
    """,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing',
    ],
    long_description=long_description
)