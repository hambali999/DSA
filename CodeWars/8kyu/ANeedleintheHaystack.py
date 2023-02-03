def find_needle(haystack):
    # your code here
    pos = []
    for x in range(len(haystack)):
        if haystack[x] == "needle":
            pos = x
    
    result = "found the needle at position {}".format(pos)
    return result