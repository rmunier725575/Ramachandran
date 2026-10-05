##  Import des librairies

import unittest
from Point_Student import Point


##  Classe de test


class Test_point(unittest.TestCase) :
    
    def test_constructeur_contruct_instance(self) :
        """
        Vérifie la création et l'initialisation de l'instance
        """
        
        #Création d'un objet vide
        pA = Point()
        self.assertIsInstance(pA, Point)
        
    
    ##  Tests sur la fonction get_abs
    
        
    def test_get_abs_1(self) :
        pA = Point()
        self.assertEqual(pA.get_abs(), 0)

    def test_get_abs_2(self) :  
        pA = Point(1,5)
        self.assertEqual(pA.get_abs(), 1)

    def test_get_abs_3(self) :  
        pA = Point(1.6,5)
        self.assertEqual(pA.get_abs(), 1.6)

    def test_get_abs_5(self) :  
        pA = Point(y=5)
        self.assertEqual(pA.get_abs(), 0)
        
    def test_get_abs_4(self) :  
        pA = Point(None,5)
        self.assertEqual(pA.get_abs(),
        
    def test_get_abs_6(self) :  
        pA = Point("ABC",5)
        self.assertEqual(pA.get_abs(), 
        
    def test_get_abs_7(self) :  
        pA = Point(180,5)
        self.assertEqual(pA.get_abs(), 180)

    def test_get_abs_8(self) :  
        pA = Point(-180,5)
        self.assertEqual(pA.get_abs(), -180)

    def test_get_abs_9(self) :  
        pA = Point(181,5)
        self.assertEqual(pA.get_abs(), 

    def test_get_abs_10(self) :  
        pA = Point(-181,5)
        self.assertEqual(pA.get_abs(), 
        
    
    ##  Tests sur la fonction get_ord
    
        
    def test_get_ord_8(self) :
        pA = Point()
        self.assertEqual(pA.get_ord(), 0)
        


##  Code principal

if __name__ == "__main__" :
    
    #Exécution des tests
    unittest.main()
