#! /usr/bin/env python3

# example script for calculating symmetry-inequivalent arrangements of 2 occupied sites in a periodic 2x2 square lattice.

# Sites in a square lattice can be represented by site labels:
# | 1 2 |
# | 3 4 |
from bsym import bsym as sym

spacegroup_filename = '../spacegroups/cubic_spacegroup_annotated'
# This contains a list of mappings between sites for all considered symmetry operations.
# e.g. 
# 1 2 3 4 (identity E: all sites unchanged)
# 2 1 4 3 (reflection in a vertical plane: site 1 moves to 2 etc.)
# 2 4 1 3 (90 degree rotation clockwise: site 1 moves to 2 etc.)

sg = sym.SpaceGroup.read_from_file( spacegroup_filename )

# how many symmetry inequivalent ways can we occupy 2 sites in a 2x2 square periodic cell?
# we define 2 occupation types with id '1' (occupied two sites) and 2 with id '0' (vacant two sites)
site_dist = { 1 : 2, 
              0 : 2 }

unique_configurations = sym.process.unique_configurations_from_sites( site_dist, sg, verbose=True )

[ config.pprint() for config in unique_configurations ] 

# Output occupationns should be equivalent to:
# 1 1 0 0 
# 1 0 0 1
# 
# These represent adjacent and diagonal occupation patterns:
# 
# 1 1 0 0 => | x x |  
#            | o o |
# 
# 1 0 0 1 => | x o |
#            | o x |





