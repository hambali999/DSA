def is_isogram(string):
    #your code here
    s = string.lower()
    return len(set(s)) == len(s)