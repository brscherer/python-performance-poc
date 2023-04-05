class Foo():
    def getter(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    def setter(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

    # property() returns a property object that implements descriptor protocol. 
    attribute1 = property(getter, setter)

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)