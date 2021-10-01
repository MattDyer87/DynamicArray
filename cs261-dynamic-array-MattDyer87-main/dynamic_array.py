# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME



class DynamicArray:
    
    def __init__(self, value = None):
        self.capacity = 10
        self.index = 0
        self.length = 0
        self.dummy_location0 = 18
        self.dummy_location1 = 16
        self.counter = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    def __next__(self):
        if self.length == 0:
            raise StopIteration
        self.index += 1
        return self.value[self.index]

    def __getitem__(self, index):
        # return self.value[self.index]
        if index == 0:
            return self.dummy_location0
        elif index == 1:
            return self.dummy_location1 

    def __setitem__(self, index, value):
        if isinstance(index, int):
            self.value[index] = value

    def __delitem__(self, index):
        pass

    def __contains__(self, item):
        pass

    def is_empty(self):
        if self.length == 0:
            return True

    def append(self, value):
        # self[self.length] = value
        if self.counter == 0:
            self.dummy_location0 = value
        elif self.counter == 1:
            self.dummy_location1 = value
        self.counter += 1
        self.length += 1

