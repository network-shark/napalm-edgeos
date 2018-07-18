"""setup.py file."""

import uuid

from setuptools import setup, find_packages
from pip.req import parse_requirements

__author__ = 'Barney Sowood <barney@sowood.co.uk>'

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="napalm-edgeos",
    version="0.1.5",
    packages=find_packages(),
    author="Barney Sowood",
    author_email="barney@sowood.co.uk",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
         'Operating System :: POSIX :: Linux',
         'Operating System :: MacOS',
    ],
    include_package_data=True,
    install_requires=reqs,
)
