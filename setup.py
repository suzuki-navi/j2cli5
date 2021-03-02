import re
from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name        = "j2cli5",
    version     = "0.0.0",
    description = "Command-line interface to Jinja2 for templating in shell scripts",
    author      = "suzuki-navi",
    packages    = find_packages(),
    install_requires = install_requirements,
    entry_points = {
        "console_scripts": [
            "j2cli5 = j2cli5.main:main",
        ]
    },
)

