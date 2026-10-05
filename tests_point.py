##  Import des librairies

import unittest
from Point_Student import Point


##  Classe de test


class Test_point(unittest.TestCase) :
    
    
    ##  Tests sur la fonction __init__()
    
    
    def test_constructeur_contruct_instance_1(self) :
        pA = Point()
        self.assertIsInstance(pA, Point)
        
    def test_constructeur_contruct_instance_2(self) :  
        with self.assertRaises(ValueError) :    
            pA = Point(None,None)

    def test_constructeur_contruct_instance_3(self) : 
        with self.assertRaises(ValueError) :    
            pA = Point("ABC","DEF")

    def test_constructeur_contruct_instance_4(self) :  
        with self.assertRaises(ValueError) :   
            pA = Point(181,181)
                                 
    def test_constructeur_contruct_instance_5(self) :  
        with self.assertRaises(ValueError) :   
            pA = Point(-181,-181)                    
                   
            
    ##  Tests sur la fonction get_abs
    
        
    def test_get_abs_1(self) :
        pA = Point()
        self.assertEqual(pA.get_abs(), 0)

    def test_get_abs_2(self) :  
        pA = Point(1,5)
        self.assertEqual(pA.get_abs(), 1)

    def test_get_abs_3(self) :  
        pA = Point(1.6,5.2)
        self.assertEqual(pA.get_abs(), 1.6)

    def test_get_abs_5(self) :  
        pA = Point(y=5)
        self.assertEqual(pA.get_abs(), 0)
        
    def test_get_abs_6(self) :  
        pA = Point(180,5)
        self.assertEqual(pA.get_abs(), 180)

    def test_get_abs_7(self) :  
        pA = Point(-180,5)
        self.assertEqual(pA.get_abs(), -180)
        
    
    ##  Tests sur la fonction get_ord
    
        
    def test_get_ord_1(self) :
        pA = Point()
        self.assertEqual(pA.get_ord(), 0)

    def test_get_ord_2(self) :  
        pA = Point(1,5)
        self.assertEqual(pA.get_ord(), 5)

    def test_get_ord_3(self) :  
        pA = Point(1.6,5.2)
        self.assertEqual(pA.get_ord(), 5.2)

    def test_get_ord_5(self) :  
        pA = Point(y=5)
        self.assertEqual(pA.get_ord(), 5)
        
    def test_get_ord_6(self) :  
        pA = Point(5,180)
        self.assertEqual(pA.get_ord(), 180)

    def test_get_ord_7(self) :  
        pA = Point(5,-180)
        self.assertEqual(pA.get_ord(), -180)


    ##  Tests sur la fonction __str__()

    
    def test_str_1(self) :
        pA = Point(1,2)
        s = "Point of coordinates (1, 2)"
        self.assertEqual(s, str(pA))   

    def test_str_2(self) :
        pA = Point(1.33333,2.333333)
        s = "Point of coordinates (1.3333, 2.3333)"
        self.assertEqual(s, str(pA))     


    ##  Tests sur la fonction add()
    

    def test_add_1(self) :
        pA = Point(0,0)
        with self.assertRaises(ValueError) :
            pA.add(1)

    def test_add_2(self) :
        pA = Point(0,0)
        with self.assertRaises(ValueError) :
            pA.add()
            
    def test_add_3(self) :
        pA = Point(0,0)
        with self.assertRaises(ValueError) :
            pA.add(None)

    def test_add_4(self) :
        pA = Point(0,0)
        with self.assertRaises(ValueError) :
            pA.add("ABC")
        
    def test_add_5(self) :
        pA = Point(0,0)
        pB = Point(1,1)
        pA.add(pB)
        expected = (1, 1)
        result = (pA.get_abs(), pA.get_ord())
        self.assertEqual(expected, result)

    def test_add_6(self) :
        pA = Point(1,2)
        pB = Point(3,4)
        pA.add(pB)
        expected = (4, 6)
        result = (pA.get_abs(), pA.get_ord())
        self.assertEqual(expected, result)

    def test_add_7(self) :
        pA = Point(1,1)
        pB = Point(180,180)
        with self.assertRaises(ValueError) :
            pA.add(pB)
            
    def test_add_8(self) :
        pA = Point(-1,-1)
        pB = Point(-180,-180)
        with self.assertRaises(ValueError) :
            pA.add(pB)
        
            
    ##  Tests pour la fonction rescale
    
    
    
    

##  Code principal


if __name__ == "__main__" :
    
    #Exécution des tests
    unittest.main()
