import time 

array1 = ['a','b','c','x']
array2 = ['z','y','i']
array3 = ['d','e','c']


''' 
Given 2 arrays, create a function
that let's a user know (true/false) whether these
two arrays contain any common items 
'''
# 1st Answer from Bali
def findCommon(arr1, arr2):
    t1 = time.time()
    for i in arr1:
        if i in arr2:
            t2 = time.time()
            print("Time taken for findCommon: {}".format(t2-t1))
            return True
    t2 = time.time()
    print("Time taken for findCommon: {}".format(t2-t1))
    return False

# 2nd Answer from Udemy
def findCommon2(arr1, arr2):
    t1 = time.time()
    for i in arr1:
        for j in arr2:
            if i == j:
                t2 = time.time()
                print("Time taken for findCommon: {}".format(t2-t1))
                return True
    t2 = time.time()
    print("Time taken for findCommon: {}".format(t2-t1))
    return False


def main():
    answer = findCommon(array1, array3)
    answer2 = findCommon2(array1, array3)

    print(answer)
    print(answer2)


main()


