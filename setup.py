import os
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)

NAME = "unicourt"
VERSION = "1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
]


setup(
    name=NAME,
    version=VERSION,
    description="UniCourt Enterprise APIs",
    author="UniCourt",
    author_email="support@unicourt.com",
    url="https://unicourt.com/",
    keywords=["UniCourt", "UniCourt Python SDK", "UniCourt Enterprise APIs"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""The UniCourt SDK provides simplified access to the UniCourt API for applications written in the Python programming language
    """
)
