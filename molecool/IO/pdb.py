"""
pdb.py

reads pdb files
"""
import numpy as py

def open_pdb(file_location):
    """
    Open and read coordinates from a pdb file

    The pdb file must specify the atom elements in the last column,
    and follow the conventions laid out in the PDB format specification

    Parameters
    ----------
    file_location : str
        The location of the pdb file to read in

    Returns
    -------
    coords : np.ndarray
        The coordinates from the pdb file.
    symbols : list
        The atomic symbols from the pdb file
    """
    with open(f_loc) as f:
        data = f.readlines()

    coordinates = []
    symbol = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbol.append(line[76:79].strip())
            atom_coordinates = [float(x) for x in l[30:55].split()]
            coordinates.append(atom_coordinates)

    # Convert list to numpy array
    coords = np.array(coordinates)

    return symbol, coords
