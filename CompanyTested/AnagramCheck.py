def anagram(s1,s2):
    
    # Remove spaces and lowercase letters
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    # Return boolean for sorted match.
    return sorted(s1) == sorted(s2)


print(anagram("dogs", "god"))
print(anagram('clint eastwood','old west action'))



def anagram2(s1,s2):
    
    # Remove spaces and lowercase letters
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    # Edge Case to check if same number of letters
    if len(s1) != len(s2):
        return False
    
    # Create counting dictionary (Note could use DefaultDict from Collections module)
    count = {}
        
    # Fill dictionary for first string (add counts)
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
            
    # Fill dictionary for second string (subtract counts)
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    # Check that all counts are 0
    for k in count:
        if count[k] != 0:
            return False

    # Otherwise they're anagrams
    return True


print(anagram2('dog','god'))
print(anagram2('clint eastwood','old west action'))


print("===")
#bali ans
def anagram3(s1, s2):
    
    s1 = sorted(s1.replace(" ",""))
    s2 = sorted(s2.replace(" ",""))
    print(s1, s2)

    
    #len must be the same anyways
    if len(s1) != len(s2):
        return False
    
    d = {} 
    
    for i in s1:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
            
    print(d)
            
    for x in s2:
        if x in d:
            d[x] -= 1
        else:
            d[x] = 1
            
    print(d)
            
    for a in d:
        if d[a] != 0:
            return False
        else:
            return True
            
print(anagram3("dog","gods"))
print(anagram3('clint eastwood','old west action'))