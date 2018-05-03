# You have a collection of generally useful methods that you would like to make available
# for extending the functionality of other class definitions. However, the classes where
# the methods might be added aren’t necessarily related to one another via inheritance.
# Thus, you can’t just attach the methods to a common base class.

class LoggedMappingMixin:
  '''
  Add logging to get/set/delete operations for debugging
  '''

  def __getitem__(self, key):
    print('Getting {}'.format(str(key)))
    return super().__getitem__(key)
  
  def __setitem__(self, key, value):
    print('Setting {} = {!r}'.format(key, value))
    return super().__setitem__(key, value)
  
  def __delitem__(self, key):
    print('Deleting {}'.format(key))
    return super().__delitem__(key)

class LoggedDict(LoggedMappingMixin, dict):
  pass