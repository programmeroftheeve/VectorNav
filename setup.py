from distutils.core import setup
from Pharlap.detect import packages_for_modalias

setup(
    name='VectorNav',
    version='0.1.0',
    author='Tim Bradt',
    author_email='tjbradt@mtu.edu',
    packages=['vectornav'],
    license='LICENSE',
    description='A Python Library for interfacing with the VectorNav IMU/GPS Solution',
    long_description=open('README.md').read(),
    install_requires=[
      "pyserial >= 2.5",
    ],
)