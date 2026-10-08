import unittest
from Atom import *
import math

class Test_Atom(unittest.TestCase):
    def test_constructeur_construct_instance(self):
        """Test that the constructor creates an instance of Atom."""
        f = Atom("N", 1, 0, 0)
        self.assertIsInstance(f, Atom)
    
    def test_norm_0(self):
        """Test the norm of an atom at the origin."""
        f = Atom("N", 0, 0, 0)
        self.assertEqual(f.norm(), 0)

    def test_norm_1(self):
        """Test the norm of an atom on the x-axis."""
        f = Atom("N", 1, 0, 0)
        self.assertEqual(f.norm(), 1)

    def test_norm_2(self):
        """Test the norm of an atom on the negative x-axis."""
        f = Atom("N", -1, 0, 0)
        self.assertEqual(f.norm(), 1)

    def test_ATOM_1(self):
        """Test the creation of an Atom instance."""
        f = Atom("N",-1.115, 8.537, 7.075)
        self.assertEqual(f.get_name(), "N")
        self.assertEqual(f.get_x(), -1.115)
        self.assertEqual(f.get_y(), 8.537)
        self.assertEqual(f.get_z(), 7.075)

    def test_ATOM_2(self):
        """Test the creation of another Atom instance."""
        f = Atom("CA", -1.925, 7.470, 6.547)
        self.assertEqual(f.get_name(), "CA")
        self.assertEqual(f.get_x(), -1.925)
        self.assertEqual(f.get_y(), 7.470)
        self.assertEqual(f.get_z(), 6.547)

    def test_ATOM_name(self):
        """Test the name of an Atom instance."""
        f = Atom("N", -1.115, 8.537, 7.075)
        g = Atom("CA", -1.925, 7.470, 6.547)
        self.assertEqual(f.get_name(), "N")
        self.assertEqual(g.get_name(), "CA")

    def test_ATOM_x(self):
        """Test the x-coordinate of an Atom instance."""
        f = Atom("N", -1.115, 8.537, 7.075)
        g = Atom("CA", -1.925, 7.470, 6.547)
        self.assertEqual(f.get_x(), -1.115)
        self.assertEqual(g.get_x(), -1.925)

    def test_ATOM_y(self):
        """Test the y-coordinate of an Atom instance."""
        f = Atom("N", -1.115, 8.537, 7.075)
        g = Atom("CA", -1.925, 7.470, 6.547)
        self.assertEqual(f.get_y(), 8.537)
        self.assertEqual(g.get_y(), 7.470)

    def test_ATOM_z(self):
        """Test the z-coordinate of an Atom instance."""
        f = Atom("N", -1.115, 8.537, 7.075)
        g = Atom("CA", -1.925, 7.470, 6.547)
        self.assertEqual(f.get_z(), 7.075)
        self.assertEqual(g.get_z(), 6.547)

    def test_ATOM_calc(self):
        """Test the calculation of atom properties."""
        f = Atom("N", -1.115, 8.537, 7.075)
        g = Atom("CA", -1.925, 7.470, 6.547)
        norm_f = math.sqrt(sum([f.get_x()**2, f.get_y()**2, f.get_z()**2]))
        norm_g = math.sqrt(sum([g.get_x()**2, g.get_y()**2, g.get_z()**2]))
        self.assertEqual(round(norm_f,2), 11.14)
        self.assertEqual(round(norm_g,2), 10.12)

    def test_ATOM_distance(self):
        """Test the distance between two atoms."""
        f = Atom("N", -1.115, 8.537, 7.075)
        g = Atom("CA", -1.925, 7.470, 6.547)
        distance = math.sqrt(sum([(f.get_x() - g.get_x())**2, (f.get_y() - g.get_y())**2, (f.get_z() - g.get_z())**2]))
        self.assertEqual(round(f.distance(g),2), 1.44)

    def test_ATOM_coordinates_distance(self):
        """Test the distance between the x-coordinates of two atoms."""
        f = Atom("N", -1.115, 8.537, 7.075)
        g = Atom("CA", -1.925, 7.470, 6.547)
        result = f.substract(g)
        self.assertEqual((round(result.get_x(), 2), round(result.get_y(), 2), round(result.get_z(), 2)), (0.81, 1.07, 0.53))

    def test_ATOM_dot_product(self):
        """Test the dot product of two atoms."""
        f = Atom("N", -1.115, 8.537, 7.075)
        g = Atom("CA", -1.925, 7.470, 6.547)
        dot_product = sum([f.get_x()*g.get_x(), f.get_y()*g.get_y(), f.get_z()*g.get_z()])
        self.assertEqual(round(f.dot_product(g),2), 112.24)

    def test_ATOM_cross_product(self):
        """Test the cross product of two atoms."""
        f = Atom("N", -1.115, 8.537, 7.075)
        g = Atom("CA", -1.925, 7.470, 6.547)
        cross_product_x = f.get_y()*g.get_z() - f.get_z()*g.get_y()
        cross_product_y = f.get_z()*g.get_x() - f.get_x()*g.get_z()
        cross_product_z = f.get_x()*g.get_y() - f.get_y()*g.get_x()
        self.assertEqual(round(cross_product_x,2), 3.04)
        self.assertEqual(round(cross_product_y,2), -6.32)
        self.assertEqual(round(cross_product_z,2), 8.10)

    def test_ATOM_angle(self):
        """Test the angle between two atoms."""
        f = Atom("N", -1.115, 8.537, 7.075)
        g = Atom("CA", -1.925, 7.470, 6.547)
        angle = math.acos(sum([f.get_x()*g.get_x(), f.get_y()*g.get_y(), f.get_z()*g.get_z()]) / (math.sqrt(sum([f.get_x()**2, f.get_y()**2, f.get_z()**2])) * math.sqrt(sum([g.get_x()**2, g.get_y()**2, g.get_z()**2]))))
        self.assertEqual(round(f.angle(g), 3), 0.095)

    def test_ATOM_copy(self):
        """Test the copy method of an Atom instance."""
        f = Atom("N", -1.115, 8.537, 7.075)
        g = Atom("CA", -1.925, 7.470, 6.547)
        h = f.copy(g)
        self.assertEqual(str(h), str(f))

    def test_ATOM_dihedral(self):
        """Test the dihedral angle between four atoms."""
        f = Atom("N", -1.115, 8.537, 7.075)
        g = Atom("CA", -1.925, 7.470, 6.547)
        h = Atom("C", -2.830, 6.390, 6.020)
        i = Atom("O", -3.640, 5.310, 5.490)
        dihedral = f.dihedral(f, g, h, i)
        self.assertEqual(round(dihedral, 3), 3.102)

    def test_ATOM_str(self):
        """Test the string representation of an Atom instance."""
        f = Atom("N", -1.115, 8.537, 7.075)
        self.assertEqual(str(f), "N (-1.11, 8.54, 7.08)")

if __name__ == '__main__':
    # Launching tests
    unittest.main()
        