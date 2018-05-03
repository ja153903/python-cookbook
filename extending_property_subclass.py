class Person:
  def __init__(self, name):
    self.name = name
  
  @property
  def name(self):
    return self._name
  
  @name.setter 
  def name(self, value):
    if not isinstance(value, str):
      raise TypeError("Expected a string")
    self._name = value
  
  @name.deleter 
  def name(self):
    raise AttributeError("Can't delete attribute")

# if we want to change multiple properties

# class SubPerson(Person):
#   @property
#   def name(self):
#     print('Getting name')
#     return super().name
  
#   @name.setter 
#   def name(self, value):
#     print('Setting name to', value)
#     super(SubPerson, SubPerson).name.__set__(self, value)
  
#   @name.deleter
#   def name(self):
#     print('Deleting name')
#     super(SubPerson, SubPerson).name.__delete__(self)

# Suppose that we only want to change one of the methods
# then we do the following:
class SubPerson(Person):
  @Person.name.getter
  def name(self):
    print('Getting name')
    return super().name