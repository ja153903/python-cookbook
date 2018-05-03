class A:
  def __init__(self):
    self._internal = 0
    self.public = 1
  
  def public_method(self):
    print("public method in A")
  
  def _internal_method(self):
    print("internal method in A")
  

class B:
  def __init__(self):
    self.__private = 0
  
  def __private_method(self):
    print("private method")
  
  def public_method(self):
    self.__private_method()
  
class C(B):
  def __init__(self):
    super().__init__()
    self.__private = 1 # does not overwrite B.__private
  
  # Does not overwrite B.__private_method()
  def __private_method(self):
    pass


  
