
class AminoAcid :


  def __init__(self, res_number, res_type, list_atoms):
    self._res_number = res_number
    self._res_type = res_type
    self._atoms = list_atoms


  def get_res_number(self):
    return self._res_number
  def get_res_type(self):
    return self._res_type
  def get_atoms(self):
    return self._atoms


  def __str__(self):
    s = "Amino acid number {} of type {} with a list of {} atoms".format(self.get_res_number(), self.get_res_type(), len(self.get_atoms()))
    return(s)   


  def add(self, atom):
    """
    Function that adds a new atom in the list of atoms for the current residue
    """
    self._atoms.append(atom)


  def get_N(self):
    """
    Function that returns an Atom corresponding to the N of the current residue
    """
    for atom in self._atoms:
      if atom.get_name() == "N":
        return atom


  def get_CA(self):
    """
    Function that returns an Atom corresponding to the CA of the current residue
    """     
    for atom in self._atoms:
      if atom.get_name() == "CA":
        return atom


  def get_C(self):
    """
    Function that returns an Atom corresponding to the C of the current residue
    """  
    for atom in self._atoms:
      if atom.get_name() == "C":
        return atom


  def get_O(self):
    """
    Function that returns an Atom corresponding to the O of the current residue
    """
    for atom in self._atoms:
      if atom.get_name() == "O":
        return atom

  # def get_atom(self, name):
  #   for atom in self._atoms:
  #         if atom.get_name() == name:
  #           return atom
  #   return None

  # def chi1(self):
  #   a1 = self.get_atom("N")
  #   a2 = self.get_atom("CA")
  #   a3 = self.get_atom("CB")
  #   a4 = self.get_atom("CG")

  #   if a1 is None or a2 is None or a3 is None or a4 is None:
  #     return None

  #   return Atom.dihedral(a1,a2,a3,a4)

  # def chi2(self):
  #   a1 = self.get_atom("CA")
  #   a2 = self.get_atom("CB")
  #   a3 = self.get_atom("CD")
  #   a4 = self.get_atom("CG")

  #   if a1 is None or a2 is None or a3 is None or a4 is None:
  #     return None

  #   return Atom.dihedral(a1,a2,a3,a4)

  # def chi3(self):
  #   a1 = self.get_atom("CB")
  #   a2 = self.get_atom("CG")
  #   a3 = self.get_atom("CD")
  #   a4 = self.get_atom("NE")

  #   if a1 is None or a2 is None or a3 is None or a4 is None:
  #     return None

  #   return Atom.dihedral(a1,a2,a3,a4)