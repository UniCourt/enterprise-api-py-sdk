# coding: utf-8

import os
from setuptools import setup, find_packages  # noqa: H301

here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)

def _read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()

def _generate_description():
    description = []
    description.append("The UniCourt Python Package provides simplified access to the UniCourt API for applications written in the Python programming language. Documentation of UniCourt's APIs can be found at docs.unicourt.com. API keys can be obtained by filling out the form here https://unicourt.com/contact-us/?c=sales&enterprise=1 \n")
    changelog_file = os.getenv("CHANGELOG_FILE")
    if changelog_file:
        description.append(_read("CHANGELOG.rst"))
    return "\n".join(description)

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "unicourt"
VERSION = "1.1.2"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.14.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Python bindings for the UniCourt Enterprise APIs",
    author="UniCourt",
    author_email="support@unicourt.com",
    license="",
    url="https://unicourt.com/",
    project_urls={
        "Source": "https://github.com/UniCourt/enterprise-api-py-sdk/tree/main",
        "Documentation": "https://docs.unicourt.com/knowledge-base/python-sdk",
    },
    keywords=["UniCourt", "UniCourt Python Package",
              "UniCourt Enterprise APIs"],
    python_requires=PYTHON_REQUIRES,
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description=_generate_description(),
    package_data={"unicourt": ["py.typed"]},
)
