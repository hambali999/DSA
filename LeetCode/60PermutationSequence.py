# Function to swap two characters in a character array
def swap(ch, i, j):
    temp = ch[i]
    ch[i] = ch[j]
    ch[j] = temp


# Recursive function to generate all permutations of a string
def permutations(ch, curr_index=0):

    if curr_index == len(ch) - 1:
        print(''.join(ch))

    for i in range(curr_index, len(ch)):
        swap(ch, curr_index, i)
        permutations(ch, curr_index + 1)
        swap(ch, curr_index, i)


if __name__ == '__main__':

    s = 'abc'
    permutations(list(s))


# https://www.techiedelight.com/find-all-permutations-string-python/

print('---')
#basically factorial
def countPermutations(data):
    print(len(data))
    # 1 = 1, 2 = 2, 3=6, 4=24

    # 1 = 1
    # 2 = 1*2
    # 3 = 1*2*3
    # 4 = 1*2*3*4
    cp = 1
    for x, i in enumerate(data):
        print(x,i)
        cp *= int(i)
    print(cp)

countPermutations('123')