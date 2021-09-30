# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME



class DynamicArray:
    
    def __init__(self):
        self.size = 10
        self.length = 0

    def __len__(self):
        return self.length

    def is_empty(self):
        if self.length == 0:
            return True

    def append(self, object):
        pass

    