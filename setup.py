import os
import sys
from setuptools import setup, find_packages

setup(
    name='phasecorr',
    version='0.1a',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['obspy',],
    author = "adienakhmad (Thomas Lecocq for setup.py)",
    author_email = "tom@asktom.be",
    description = "Phase CC",
    license = "MIT",
    url = "https://github.com/adienakhmad/phasecorr",
    keywords="phase cross-correlation, phase autocorrelation"
)