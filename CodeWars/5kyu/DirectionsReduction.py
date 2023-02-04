import unittest

def dirReduc(arr):
    opposite = {"NORTH":"SOUTH", "SOUTH":"NORTH", "EAST":"WEST", "WEST":"EAST"}
    tracker = [] #stack
    for x in arr:
        if tracker == []:
            tracker.append(x)
        else:
            if tracker[-1] == opposite[x]:
                tracker.pop()
            else:
                tracker.append(x)
    return tracker


class Test(unittest.TestCase):
    def test_two(self):
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
        self.assertEqual(dirReduc(a), ['WEST'])

if __name__=='__main__':
	unittest.main()

