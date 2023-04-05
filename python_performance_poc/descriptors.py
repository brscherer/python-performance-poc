# descriptors.py

# Descriptors are classes that has specific behaviors when used as class attributes
# They are instantiated just once per class.
# That means that every single instance of a class containing descriptors shares that descriptor instance
class Verbose_attribute():
  # __get__ has `type` variable because it can be called on both the object and the class
  def __get__(self, obj, type=None) -> object:
    # we can capture exact moment a descriptor is accessed and log it if needed
    print("accessing the attribute to get the value")
    return 42
  # Recommended way to implement read-only descriptors is by raising an AttributeError exception when accessed to .__set__()
  def __set__(self, obj, value) -> None:
    print("accessing the attribute to set the value")
    raise AttributeError("Cannot change the value")

class Foo():
  attribute1 = Verbose_attribute()

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)

# Useful for Lazy Properties, which are properties whose initial values are not loaded until they're accessed for the first time.
# Then they load their initial value and keep that value cached for later reuse
import time

class DeepThought:
    def meaning_of_life(self):
        time.sleep(3)
        return 42

my_deep_thought_instance = DeepThought()
print(my_deep_thought_instance.meaning_of_life())
print(my_deep_thought_instance.meaning_of_life())
print(my_deep_thought_instance.meaning_of_life())

# Next approach will cache the value and will sleep only in the first time it gets called
# Thats because it is a `non-data descriptor`, which means it only implements `__get__`

import time

class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]
      
    # Uncommenting next line would transform this descriptor in a data descriptor
    # data descriptors have precedence non-over data descriptors in the python lookup chain, so it wouldn't wait to check in the __dict__
    # thats why it not work when we implement __set__, turning this descriptor into a data descriptor
  
    # def __set__(self, obj, value):
    #   pass

class DeepThought:
    @LazyProperty
    def meaning_of_life(self):
        time.sleep(3)
        return 42

my_deep_thought_instance = DeepThought()
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)