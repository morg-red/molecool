"""
molecool
A python package for viewing and analyzing certain files
"""

# Add imports here
from .functions import *
from .measure import calculate_angle, calculate_distance
from .visualize import draw_molecule, draw_bond_histogram
from .molecule import build_bond_list
from .atom_data import atomic_weights, atom_colors

import molecool.IO

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
