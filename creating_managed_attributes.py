class Person:
  def __init__(self, first_name):
    self.first_name = first_name
  
  # Getter function
  @property
  def first_name(self):
    return self._first_name
  
  # Setter function
  @first_name.setter 
  def first_name(self, value):
    if not isinstance(value, str):
      raise TypeError("Expected a string")
    self._first_name = value
  
  # Deleter function
  @first_name.deleter 
  def first_name(self):
    raise AttributeError("Can't delete attribute")

import math
class Circle:
  def __init__(self, radius):
    self.radius = radius
  
  @property
  def radius(self):
    return self._radius
  
  @radius.setter 
  def radius(self, value):
    if not isinstance(value, float) or not isinstance(value, int):
      raise TypeError("Needs a float or int value")
    self._radius = value
  
  @property
  def area(self):
    return math.pi * self.radius ** 2
  
  @property
  def perimeter(self):
    return 2 * math.pi * self.radius