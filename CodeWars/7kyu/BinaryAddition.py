# Binary Addition
# Basically converting decimal to binary..

def add_binary(a,b):
    #your code here
    sum = bin(a +b)
    return sum.replace('0b',"")


def add_binary(a,b):
    sum = a+b
    binList = []
    # print(sum)
    while sum > 0:
        binList.append(sum%2)
        sum = sum//2
        print(sum)
    print(binList)
    print(''.join([str(x) for x in binList[::-1]]))


add_binary(2,3)
