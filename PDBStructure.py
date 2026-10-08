#Import library
from AminoAcid import AminoAcid
from Atom import Atom
from Point import Point


class StructurePDB:

  def __init__(self, filename):
    """
    Functions that reads a simple PDB file and the necessary information about residues to compute dihedral angles
    """
    self.__path_to_file = filename
    self.__residues = []    # liste d'AminoAcid, dans l'ordre du fichier
    self.__phi = []         # angle phi du résidu i (Si non None)
    self.__psi = []         # angle psi du résidu i (Si non None)
    self.__phipsi = []      # liste de Point(phi, psi)

    with open(self.__path_to_file, 'r') as fd:
      lines = []
      for line in fd:
        lines.append(line.split())

    previous_res_number = None
    aa = None

    for line in lines:

      if len(line) == 0:
        continue

      if len(line) < 9:
        continue

      if line[0] != "ATOM":
        continue

      atom_type = line[2]
      if atom_type not in ["N", "CA", "C", "O"]:
        continue

      residue_type = line[3]
      residu_number = int(line[5])

      if previous_res_number != residu_number:
        aa = AminoAcid(residue_type, residu_number, [])
        self.__residues.append(aa)
        previous_res_number = residu_number

      coordX = float(line[6])
      coordY = float(line[7])
      coordZ = float(line[8])

      atom = Atom(atom_type, coordX, coordY, coordZ)
      aa.add(atom)


  def get_residues(self):
    return self.__residues

  def get_phi(self):
    return self.__phi

  def get_psi(self):
    return self.__psi

  def get_phipsi(self):
    return self.__phipsi


  def compute_dihedrals(self):
    """
    Functions that computes dihedral angles
    phi(i) : C(i-1) - N(i)  - CA(i) - C(i)
    psi(i) : N(i)   - CA(i) - C(i)  - N(i+1)
    """
    self.__phi = []
    self.__psi = []
    self.__phipsi = []

    residues = self.get_residues()
    length = len(residues)

    for i in range(length):

      current_aa = residues[i]

      if i == 0:
        phi_value = None
      else:
        previous_aa = residues[i - 1]
        phi_value = Atom.dihedral(previous_aa.get_C(), current_aa.get_N(),current_aa.get_CA(), current_aa.get_C())

      if i == length - 1:
        psi_value = None
      else:
        next_aa = residues[i + 1]
        psi_value = Atom.dihedral(current_aa.get_N(), current_aa.get_CA(),current_aa.get_C(), next_aa.get_N())

      self.__phi.append(phi_value)
      self.__psi.append(psi_value)

      if phi_value is not None and psi_value is not None:
        self.__phipsi.append(Point(phi_value, psi_value))


  def write_dihedrals(self, filename):
    """
    Functions that writes a file with 2 columns phi and psi separated by a tabulation, with one line per residue. Values of phi and psi angles are given with a precision of 6 decimals.
    """
    with open(filename, 'w') as fd:
      for point in self.get_phipsi():
        fd.write(f"{point.get_abs():.6f}\t{point.get_ord():.6f}\n")


#-------------------------------------------------------------------------------------------------------------

### Program ###


iS = StructurePDB("1TEY.pdb")
print(iS.residues[0])
print(iS.residues[1])
print(iS.residues[2])
iS.compute_dihedrals()
iS.write_dihedrals("angles_1TEY.txt")