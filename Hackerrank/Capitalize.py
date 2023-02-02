def capitalize(s):
    for x in s.split():
        s = s.replace(x, x.capitalize())
    return s



print(capitalize("chris alan"))