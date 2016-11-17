from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from setuptools import setup, find_packages

__author__ = 'Tim Martin'
__pkg_name__ = 'framework'

version = '0.0.1'

setup(
    author=__author__,
    author_email='martin@apptimize.com',
    description='An example Flask setup',
    name='apptimize-test-framework',
    packages=find_packages(include=['myapp', 'myapp*']),
    test_suite="myapp_tests",
    version=version
)
