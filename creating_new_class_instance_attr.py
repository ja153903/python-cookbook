class Integer:
  def __init__(self, name):
    self.name = name
  
  def __get__(self, instance, cls):
    if instance is None:
      return self
    else:
      return instance.__dict__[self.name]
  
  def __set__(self, instance, value):
    if not isinstance(value, int):
      raise TypeError("Expected an int")
    # it would be something like that
    # instance.d['x'] = 4
    # instance.d['y'] = 5
    instance.__dict__[self.name] = value
  
  def __delete__(self, instance):
    del instance.__dict__[self.name]
  
class Point:
  x = Integer('x')
  y = Integer('y')
  def __init__(self, x, y):
    self.x = x
    self.y = y


class Person:
  def __init__(self, name):
    self.name = name
  
  def __get__(self, instance, cls):
    if instance is None:
      return self
    else:
      return instance.__dict__[self.name]
  
  def __set__(self, instance, value):
    if not isinstance(value, str):
      raise TypeError("Expected a string")
    instance.__dict__[self.name] = value

class SubPerson:
  name = Person('name')
  college = Person('college')
  def __init__(self, name, college):
    self.name = name
    self.college = college

# Descriptor for a type-checked attribute
class Typed:
  def __init__(self, name, expected_type):
    self.name = name
    self.expected_type = expected_type
  
  def __get__(self, instance, cls):
    if instance is None:
      return self
    else:
      return instance.__dict__[self.name]
    
  def __set__(self, instance, value):
    if not isinstance(value, self.expected_type):
      raise TypeError("Expected " + str(self.expected_type))
    instance.__dict__[self.name] = value
  
  def __delete__(self, instance):
    del instance.__dict__[self.name]

# class decorator that applies it to selected attributes
def typeassert(**kwargs):
  def decorate(cls):
    for name, expected_type in kwargs.items():
      # Attach a Typed descriptor to the class
      setattr(cls, name, Typed(name, expected_type))
    return cls
  return decorate

# this decorator will throw if we put invalid types
@typeassert(name=str, shares=int, price=float)
class Stock:
  def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price