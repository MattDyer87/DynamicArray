# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME



class DynamicArray:
    
    def __init__(self):
        self.size = 10

    def is_empty(self):
        if self.len() == 0:
            return True

    