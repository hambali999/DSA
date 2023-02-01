# Unique Characters in String

## Problem
# Given a string,determine if it is compreised of all unique characters. 
# For example, the string 'abcde' has all unique characters and should return True. 
# The string 'aabcde' contains duplicate characters and should return false.


def uni_char(s):
    print(s)
    s = sorted(s)
    for x in range(len(s)-1):
        # print(s[x], s[x+1])
        if s[x] == s[x+1]:
            return False
    return True


print(uni_char("abcdefg"))

# another method 
def uni_char(s):
    return len(set(s)) == len(s)
    
# another method 
def uni_char2(s):
    chars = set()
    for let in s:
        # Check if in set
        if let in chars:
            return False
        else:
            #Add it to the set
            chars.add(let)
    return True