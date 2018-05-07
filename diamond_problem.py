class BaseClass:
  num_base_calls = 0
  def call_me(self):
    print("Calling method in BaseClass")
    self.num_base_calls += 1

class LeftSubClass(BaseClass):
  num_left_calls = 0
  def call_me(self):
    super().call_me()
    print("Calling method in LeftSubClass")
    self.num_left_calls += 1

class RightSubClass(BaseClass):
  num_right_calls = 0
  def call_me(self):
    super().call_me()
    print("Calling method in RightSubClass")
    self.num_right_calls += 1

class SubClass(LeftSubClass, RightSubClass):
  num_sub_calls = 0
  def call_me(self):
    super().call_me()
    print("Calling method in SubClass")
    self.num_sub_calls += 1

'''
Note that when we print this out we get the following output

Calling method in BaseClass
Calling method in RightSubClass
Calling method in LeftSubClass
Calling method in SubClass

Note that this happens because when we call super().call_me()
in the LeftSubclass it's not calling the call_me() in BaseClass
but rather it's calling the RightSubClass's call_me().
This is because it's calling the next method and not the parent method

This is super important for final
'''