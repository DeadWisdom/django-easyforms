"""
Django Easy Forms setup.
"""

from setuptools import setup, find_packages

setup( name='easyforms',
       version='0.1',
       description='Django app for easier forms.',
       author='Brantley Harris',
       author_email='brantley.harris@gmail.com',
       packages = find_packages(),
       include_package_data = True,
       zip_safe = False,
      )
