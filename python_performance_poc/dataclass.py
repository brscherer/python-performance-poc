# Reference video link: https://www.youtube.com/watch?v=Fot3_9eDmOs

import timeit

# using dataclasses makes easier to use slots and avoid duplicating attributes name an setting them
from dataclasses import dataclass
from functools import partial

@dataclass(slots=False)
class Person:
  name: str
  address: str
  email: str
    

# limit attributes that can be assigned to instances of the class
# resulting in memory savings and faster attribute access
@dataclass(slots=True)
class PersonSlots:
  name: str
  address: str
  email: str
  
    
def get_set_delete(person):
  person.address = "Brazil"
  _ = person.address
  del person.address
    
    
def main():
  person = Person("Bruno", "Brazil", "bruno@email.com")
  person_slots = PersonSlots("Bruno", "Brazil", "bruno@email.com")
  no_slots = min(timeit.repeat(partial(get_set_delete, person), number=1000000))
  slots = min(timeit.repeat(partial(get_set_delete, person_slots), number=1000000))
  print(f"No slots: {no_slots}")
  print(f"Slots: {slots}")
  print(f"% performance improvement: {(no_slots - slots) / no_slots:.2%}")
  
if __name__ == "__main__":
  main()


# Why slots are not a default in python?
#
# 1. Slots were not supported initially but added after into python, 
# it means it would need to change a core piece of the language and high risk to break old implementations
#
# 2. It has some limitations
# 2.1. Cannot use mixins or multiple inheritances, although using them is not a good idea
# 2.2. Cannot dynamically add attributes to classes, which also isn't good because you loose reliability to code, you don't know which structure it can become.
