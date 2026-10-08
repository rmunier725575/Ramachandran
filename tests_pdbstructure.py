##  Import des librairies

import unittest
from PDBStructure_Student import StructurePDB
from AminoAcid import AminoAcid
import math


##  Classe de test


class Test_pdbstructure(unittest.TestCase) :


    ##  Tests pour la fonction __init__()


    def test_constructeur_contruct_instance_1(self) :
        with self.assertRaises(ValueError) :
            pdb_file = StructurePDB("")

    def test_constructeur_contruct_instance_2(self) :
        with self.assertRaises(ValueError) :
            pdb_file = StructurePDB("abc")

    def test_constructeur_contruct_instance_3(self) :
        with self.assertRaises(ValueError) :
            pdb_file = StructurePDB(None)

    def test_constructeur_contruct_instance_4(self) :
        pdb_file = StructurePDB("1tey_model1.pdb")
        self.assertIsInstance(pdb_file, StructurePDB)
        results_residues = pdb_file.__residues
        self.assertTrue(all([isinstance(r, AminoAcid) for r in results_residues]))


##  Code principal


if __name__ == "__main__" :
    
    #Exécution des tests
    unittest.main()
