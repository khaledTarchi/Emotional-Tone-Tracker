class MyClassWithoutSlots:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class MyClassWithSlots:
    __slots__ = ['a', 'b']

    def __init__(self, a, b):
        self.a = a
        self.b = b


import sys

instance_without_slots = MyClassWithoutSlots(1, 2)
print("Memory usage without slots:", sys.getsizeof(instance_without_slots.__dict__))

instance_with_slots = MyClassWithSlots(1, 2)
print("Memory usage with slots:", sys.getsizeof(instance_with_slots))
