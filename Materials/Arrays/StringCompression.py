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

# compress('AABBCC')
compress('AAABCCDDDDD')


def string_compression(input_string):
    out = ""
    string = input_string
    counter = 0 #  assign counter to zero
    for i in range(0, len(string)-1):
        # checks current letter and next letter  are same or not if same counter  increments
        if string[i] == string[i+1]:
             counter += 1
        else:
            # else condition run if next letter is not matched with current letter
            counter += 1
            out += f'{string[i]}{counter}'
            counter = 0
    #for last letter to be added it is incremented and added to out string
    counter += 1
    out += f'{string[i+1]}{counter}'
    print(out)

string_compression('AAABCCDDDDDE')
