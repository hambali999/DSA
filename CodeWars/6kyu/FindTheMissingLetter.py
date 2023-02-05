# Find the missing letter
# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.

# Example:

# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'

import unittest

#bali ans
def find_missing_letter(chars):
    checkcasing = True if chars[0].upper() == chars[0] else False
    chars = [x.lower() for x in chars]
    alb = list(map(chr, range(97, 123)))
    start = chars[0]
    end = chars[-1]
    correctsum = []
    sum = []
    for i in range(len(alb)):
        if alb[i] in chars:
            print(alb[i])
            sum.append(alb[i])
    print('===')
    for x in range(alb.index(start),alb.index(end)+1):
        print(alb[x])
        correctsum.append(alb[x])
    print("===")
    for x in correctsum:
        if x not in sum:
            if checkcasing == True:
                return x.upper()
            else:
                return x

def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))

def find_missing_letter(input):
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    start = alphabet.index(input[0])
    for i in range(len(input)):
        if not input[i] == alphabet[start+i]:
            return alphabet[start+i]
    
        
class Test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(find_missing_letter(['O','Q','R','S']), 'P')
    def test_two(self):
        self.assertEqual(find_missing_letter(['a','b','c','d','f']), 'e')
    

if __name__=='__main__':
	unittest.main()

        

