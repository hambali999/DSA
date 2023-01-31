#bali's answer
def compress(s):
    print(s)

    d = {}

    for x in s:
        # print(x)
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1

    # print(d)
    items = ' '.join(f'{key} {value}' for key, value in d.items()).replace(" ", "")
    print(items)
    print("\n")

compress('AABBCC')
compress('AAABCCDDDDD')