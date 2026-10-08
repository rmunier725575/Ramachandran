import unittest
from Atom import *
from AminoAcid import *
import math

class Test_AminoAcid(unittest.TestCase):
    def test_constructeur_construct_instance(self):
        """Test that the constructor creates an instance of AminoAcid."""
        f = AminoAcid(1,"MET",[Atom("N", 0, 0, 0), Atom("CA", 1, 0, 0), Atom("C", 2, 0, 0), Atom("O", 3, 0, 0)])
        self.assertIsInstance(f, AminoAcid)
    
    def test_AminoAcid_name(self):
        """Test the name of an AminoAcid instance."""
        f = AminoAcid(1,"MET",[Atom("N", 0, 0, 0), Atom("CA", 1, 0, 0), Atom("C", 2, 0, 0), Atom("O", 3, 0, 0)])
        self.assertEqual(f.get_res_type(), "MET")

    def test_AminoAcid_get_N(self):
        """Test the N atom of an AminoAcid instance."""
        f = AminoAcid(1,"MET",[Atom("N", 0, 0, 0), Atom("CA", 1, 0, 0), Atom("C", 2, 0, 0), Atom("O", 3, 0, 0)])
        self.assertEqual(f.get_N().get_name(), "N")

    def test_AminoAcid_get_CA(self):
        """Test the CA atom of an AminoAcid instance."""
        f = AminoAcid(1,"MET",[Atom("N", 0, 0, 0), Atom("CA", 1, 0, 0), Atom("C", 2, 0, 0), Atom("O", 3, 0, 0)])
        self.assertEqual(f.get_CA().get_name(), "CA")

    def test_AminoAcid_get_C(self):
        """Test the C atom of an AminoAcid instance."""
        f = AminoAcid(1,"MET",[Atom("N", 0, 0, 0), Atom("CA", 1, 0, 0), Atom("C", 2, 0, 0), Atom("O", 3, 0, 0)])
        self.assertEqual(f.get_C().get_name(), "C")

    def test_AminoAcid_get_O(self):
        """Test the O atom of an AminoAcid instance."""
        f = AminoAcid(1,"MET",[Atom("N", 0, 0, 0), Atom("CA", 1, 0, 0), Atom("C", 2, 0, 0), Atom("O", 3, 0, 0)])
        self.assertEqual(f.get_O().get_name(), "O")

    def test_AminoAcid_str(self):
        """Test the string representation of an AminoAcid instance."""
        f = AminoAcid(1,"MET",[Atom("N", 0, 0, 0), Atom("CA", 1, 0, 0), Atom("C", 2, 0, 0), Atom("O", 3, 0, 0)])
        self.assertEqual(str(f), "Amino acid number 1 of type MET with a list of 4 atoms")

    def test_AminoAcid_add(self):
        """Test the add method of an AminoAcid instance."""
        f = AminoAcid(1, "MET", [Atom("N", 0, 0, 0), Atom("CA", 1, 0, 0), Atom("C", 2, 0, 0), Atom("O", 3, 0, 0)])
        f.add(Atom("H", 4, 0, 0))
        g = Atom("Fe", 5, 0, 0)
        f.add(g)
        atoms = f.get_atoms()
        self.assertEqual(len(atoms), 6)
        self.assertEqual(atoms[4].get_name(), "H")
        self.assertIs(atoms[5], g)

