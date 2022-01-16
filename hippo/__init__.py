# -*- coding: utf-8 -*-
import pkg_resources  # type: ignore
from pathlib import Path

# get the directory to the package base
# i.e. the folder containing the __init__.py module
PACKAGE_BASE = Path(__file__).parent
__version__ = pkg_resources.get_distribution(PACKAGE_BASE.name).version
