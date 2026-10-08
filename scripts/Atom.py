from math import sqrt 
from math import acos
from math import atan2


class Atom:
  def __init__(self, name, px = 0.00, py = 0.00, pz = 0.00):
    self._name = name
    self._x = px
    self._y = py 
    self._z = pz

	
  def set_name(self, pname):
    """
    Function that modifies the name
    """
    self._name = pname
 	

  def set_coords(self, px, py, pz):
    """
    Function that modifies the attributes x, y, z
    """
    self._x = px
    self._y = py
    self._z = pz


  def get_name(self):
    """
    Function that returns the name of the atom as a string
    """
    return self._name

    
  def get_coords(self):
    """
    Function that returns a list containing the coodinates (x,y,z)
    """
    return [(self._x, self._y, self._z)]
    
  def get_x(self):
    """
    Function that returns the x coordinate
    """
    return self._x

    
  def get_y(self):
    """
    Function that returns the y coordinate
    """
    return self._y

  
  def get_z(self):
    """
    Function that returns the z coordinate
    """
    return self._z


  def copy(self, another_atom):
    """
    Function that copies the values of the current instance in a new atom passed as a parameter
    """
    another_atom.set_name(self.get_name())
    another_atom.set_coords(self.get_x(), self.get_y(), self.get_z())
  
  
  def __str__(self):
    s = "{} ({:.2f}, {:.2f}, {:.2f})".format(self.get_name(), self.get_x(), self.get_y(), self.get_z())
    return(s)
	
	
  def norm(self):
    """
    Function that computes the norm of the vector from O to the current instance
    """
    return sqrt((int(self.get_x())**2) + (int(self.get_y())**2) + (int(self.get_z())**2))
	
	
  def distance(self, another_atom):
    """
    Function that computes the distance between the current instance and another atom
    """
    de = sqrt((self.get_x()- another_atom.get_x())**2 + (self.get_y() - another_atom.get_y())**2 + (self.get_z() - another_atom.get_z())**2)
    return de


  def substract(self, another_atom):
    """
    Function that computes the substraction between the current atom and the other atom passed as a parameter, and returns it as a new Atom with an empty name.
    """
    sub_x = (self.get_x()) - (another_atom.get_x())
    sub_y = (self.get_y()) - (another_atom.get_y())
    sub_z = (self.get_z()) - (another_atom.get_z())

    return Atom("",sub_x, sub_y, sub_z)

	
  def dot_product(self, another_atom):
    """
    Function that computes the dot product between the current atom and the other atom passed as a parameter, and returns it as a float
    """
    dot = (self.get_x()*another_atom.get_x()) + (self.get_y()*another_atom.get_y()) + \
      (self.get_z()*another_atom.get_z())
    return dot


  def cross_product(self, another_atom):
    """
    Function that computes the cross product between the current atom and the other atom passed as a parameter, and returns it as a new Atom with an empty name.
    """
    cross_x = (self.get_y() * another_atom.get_z()) - (self.get_z() * another_atom.get_y())
    cross_y = (self.get_z() * another_atom.get_x()) - (self.get_x() * another_atom.get_z())
    cross_z = (self.get_x() * another_atom.get_y()) - (self.get_y() * another_atom.get_x())
    return Atom("",cross_x,cross_y,cross_z)

    
  def angle(self, another_atom):
    """
    Function that computes the the angle between two sets of coordinates
    """
    return acos(self.dot_product(another_atom)/(self.norm()*another_atom.norm()))
	

  def dihedral(self, a1, a2, a3, a4):
    """
    Function that computes dihedral angle (torsion angle) between 4 atoms named a1 to a4
    """
    #calcul de vecteurs
    b1 = a2.substract(a1)
    b2 = a3.substract(a2) #liaison centrale
    b3 = a4.substract(a3)
	
	  #calcul des vecteurs normaux (b1xb2 = normal au plan a1a2a3)pour trouver l’angle entre deux plans
    n1 = b1.cross_product(b2)
    n2 = b2.cross_product(b3)
	
    #formule : (x_cosinus = - norm de b2 * produit scalaire b1 et n2, y_sinus = produit scalaire n1 et n2)
    #atan2 calcul angle a partir de 2 valeurs
    return atan2(-b2.norm()*b1.dot_product(n2), n1.dot_product(n2))

  def dihedral_lat(chi1, chi2, chi3, chi4, chi5):
    pass



if __name__ == "__main__":	
  print("Testing Class Atom")
  atom1 = Atom("H",18.0,9.5,192.5)
  atom2 = Atom("C",18.0,9.5,0)
  atom3 = Atom("O",0,0,1)
  atom4 = Atom('N',2.96,5.2,7.4)
  another_atom = Atom("C",3,4,5)
  
  print(atom1)
  print(atom2)
  print(atom3)
  print(another_atom)

  print(atom1.dihedral( atom2, atom3, atom4))

  print(atom1.norm())

  atom1.copy(another_atom)
  print(another_atom)