def capitalize(s):
    # print(s.split())
    for x in s.split():
        print(x)
        s = s.replace(x, x.capitalize())
        # print(x)
    return s



print(capitalize("chris alan"))