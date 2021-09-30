# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME



class DynamicArray:
    
    def __init__(self):
        self.capacity = 10
        self.index = 0
        self.length = 0

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
        return 64

    # def __setitem__(self, index, value):
    #     if isinstance(index, int):
    #         self.value[index] = value

    def __delitem__(self, index):
        pass

    def __contains__(self, item):
        pass

    def is_empty(self):
        if self.length == 0:
            return True

    def append(self, value):
        # self[self.length] = value
        self.length += 1

