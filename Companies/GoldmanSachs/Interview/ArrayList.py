class ArrayList:
    def __init__(self):
        self.array = []

    def append(self, value):
        self.array.append(value)

    def get(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            raise IndexError("Index out of range")

    def size(self):
        return len(self.array)

# Example usage:
my_list = ArrayList()
my_list.append(1)
my_list.append(2)
my_list.append(3)

print("List:", my_list.array)
print("Element at index 1:", my_list.get(1))
print("Size:", my_list.size())
