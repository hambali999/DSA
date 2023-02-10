# So Many Permutations!
# input='aabb' = return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
# abc = abc,acb,bca,bac,cba,cab
# https://www.techiedelight.com/find-all-permutations-string-python/

import itertools


# def permutations(string):
#     result = set([string])
#     print(result)

#     if len(string) == 2:
#         result.add(string[1] + string[0])

#     elif len(string) > 2:
#         for i, c in enumerate(string):
#             print(i,c)
#             for s in permutations(string[:i] + string[i + 1:]):
#                 result.add(c + s)

#     return list(result)

def permutations(string):
    if len(string) == 1: return set(string)
    first = string[0]
    rest = permutations(string[1:])
    result = set()
    for i in range(0, len(string)):
        for p in rest:
            result.add(p[0:i] + first + p[i:])
            # print(p[0:i] + first + p[i:])
            # print('---')
    return list(result)

def permutations(string):
    # Code Away!
    result = set([string])
    # print(result)

    if len(string) == 2:
        result.add(string[1] + string[0])

    elif len(string) > 2:
        for i, c in enumerate(string):
            print(i,c)
            for s in permutations(string[:i] + string[i + 1:]):
                print(s)
                result.add(c + s)
            print('===')

    return list(result)





print("start")
print(permutations('abcd'))
print(len(permutations('abc')))



