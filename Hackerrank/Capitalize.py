def capitalize(s):
    # print(s.split())
    for x in s.split():
        # print(x)
        s = s.replace(x, x.capitalize())
    return s



print(capitalize("chris alan"))