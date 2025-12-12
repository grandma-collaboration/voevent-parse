#!/usr/bin/env python

from setuptools import find_packages, setup
import versioneer

install_requires = [
    "astropy>=1.2",
    "lxml>=2.3",
    'iso8601',
    'orderedmultidict',
    'pytz',
]

test_requires = [
    'pytest>3',
    'coverage'
]

extras_require = {
    'test': test_requires,
    'all': test_requires,
}


classifiers = [
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "Intended Audience :: Science/Research",
]

setup(
    name="voevent-parse",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    package_data={'voeventparse': ['fixtures/*.xml']},
    description="Convenience routines for parsing and manipulation of "
                "VOEvent XML packets.",
    author="Tim Staley",
    author_email="github@timstaley.co.uk",
    url="https://github.com/timstaley/voevent-parse",
    python_requires='>=3.8',
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=classifiers
)
