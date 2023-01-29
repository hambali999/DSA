class MyHashSet(object):
    def __init__(self):
        self.s = []

    def add(self, key):
        self.s.append(key)

    def remove(self, key):
        count = 0
        for i in range(len(self.s)):
            if self.s[i] == key:
                count += 1
                for x in range(count):
                    self.s.remove(key)

    def contains(self, key):
        if key in self.s:
            return True
        else:
            return False
