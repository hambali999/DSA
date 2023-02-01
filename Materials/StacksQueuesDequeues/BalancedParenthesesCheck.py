def balance_check(s):
    # print(s)
    d = {}

    for x in s:
        if x not in d:
            d[x] = 0
        elif x == "[":
            d[x] += 1
        elif x == "]":
            d["["] -= 1
        elif x == "(":
            d[x] += 1
        elif x == ")":
            d["("] -= 1

    for k,v in d.items():
        # print(k,v)
        if v != 0:
            return False
        else:
            return True



print(balance_check("[]]["))