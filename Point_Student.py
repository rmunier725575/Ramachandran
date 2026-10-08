# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:07:20 2020, Modifié le Oct 05 14:24

@authors: ebecker, ldebray, mcouvrat
"""

#Import library
from math import sqrt

"""
Class point define points in a 2D plan.

Entry : x and y coordonate of a point.
"""
class Point:
  ### Initialization ###
  def __init__(self, x = 0.00, y = 0.00):
    self._abs = x
    self._ord = y

    # Raise ValueError if coordonate is None or a str()
    if self._abs is None or self._ord is None:
      raise ValueError("L'ordonné ou l'abscise ne peut pas être None")
    if self._abs is str() or self._ord is str():
      raise ValueError("L'ordonné ou l'abscise ne peut pas être un str()")

  ### Print Method ###
  def __str__(self):
    return "Point of coordinates ({}, {})".format(round(self.get_abs(), 4), round(self.get_ord(), 4))

  ### Acceseurs ###
  def get_abs(self):
    return self._abs
	
  def get_ord(self):
    return self._ord

  ### Method ###
  def add(self, another_point):
    """
    Functions that adds to the current Point to another point passed as an argument
    """
    self._ord += another_point.get_ord()
    self._abs += another_point.get_abs()
    return None


  def rescale(self, factor):
    """
    Functions that rescales the current Point by a scalar passed as an argument
    """
    self._ord = self.get_ord() * factor
    self._abs = self.get_abs() * factor
    return None

  def distance_from_origin(self):	
    """
    Functions that computes the distance of the current Point to the origin of the plan O. Calculated with euclidian distance.
    """
    distance_orig = sqrt((self.get_abs())**2 + (self.get_ord())**2)
    return distance_orig


  def euclidean_distance(self, another_point):
    """
    Functions that computes the euclidean distance of the current Point with another point passed as an argument
    """
    distance_eucli = sqrt((self.get_abs() - another_point.get_abs())**2 + (self.get_ord() - another_point.get_ord())**2)
    return distance_eucli
  
  def manhattan_distance(self, another_point):
    """
    Functions that computes the manhattan distance of the current Point with another point passed as an argument
    """
    distance_man = abs(self.get_abs() - another_point.get_abs()) + abs(self.get_ord() - another_point.get_ord())
    return distance_man


#-------------------------------------------------------------------------------------------------------------

"""

Class ClusterPoint is a subclass of Class Point, with the add of the attribute num_cluster, corresponding to the number of the cluster.

"""

class ClusterPoint(Point):
  def __init__(self, num_cluster):
    Point(self)
    self._num_cluster = num_cluster

  def get_num_cluster(self):
    return self._num_cluster



#-------------------------------------------------------------------------------------------------------------

### Program ###

if __name__ == "__main__":	
  pA = Point(0,0)
  pB = Point(1,1)
  pC = Point(2,1)
  pD = Point(3,4)

  print(pA)
  print(pB)
  print(pC)
  print(pD)

  pA.add(pB)
  assert pA.get_abs() == 1, 'Error in Point.add'
  print(pA.get_abs())
  pA.rescale(5)
  print(pA.get_abs())
  assert pA.get_abs() == 5, 'Error in Point.rescale'
  
  assert pD.distance_from_origin() == 5, 'Error in Point.distance_from_origin'
  assert pB.euclidean_distance(pC) == 1, 'Error in Point.distance'
  assert pB.manhattan_distance(pC) == 1, 'Error in Point.distance'

