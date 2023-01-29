

class MyHashMap:
    def __init__(self):
        self.hashMap = []

    def put(self, key: int, value: int) -> None:
        key_value = []
        key_value.append(key)
        key_value.append(value)
        for element in self.hashMap:
            if element[0] == key:
                element[1] = value
                return self
            return self.hashMap.append(key_value)

    def get(self, key: int) -> int:
        for element in self.hashMap:
            if element[0] == key:
                return element[1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.hashMap)):
            if self.hashMap[i][0] == key:
                self.hashMap.pop(i)
                return self.hashMap
            return self.hashMap

# Input

# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]

# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

# Output

# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation

# MyHashMap myHashMap = new MyHashMap();

# myHashMap.put(1, 1); // The map is now [[1,1]]

# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]

# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]

# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]

# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)

# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]

# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]

# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
