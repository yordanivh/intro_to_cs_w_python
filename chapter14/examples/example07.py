from example06 import Molecule
from example05 import Atom
from typing import TextIO

def read_molecule(r: TextIO) -> Molecule:
    """Read a single molecule from r and return it,
    or return None to signal end of file.
    """
    # If there isn't another line, we're at the end of the file.
    line = r.readline()
    if not line:
        return None

    # Name of the molecule: "COMPND name"
    key, name = line.split()

    # Other lines are either "END" or "ATOM num kind x y z"
    molecule = Molecule(name)
    reading = True

    while reading:
        line = r.readline()
        if line.startswith('END'):
            reading = False
        else:
            key, num, kind, x, y, z = line.split()
            molecule.add(Atom(int(num),kind, float(x), float(y), float(z)))
    return molecule

