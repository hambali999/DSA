import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'bloat', 'nigel', 'squirt','bloat', 'nigel', 'squirt', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla']
large = ['dory' for i in range(100000)]
large.append('nemo')
def find_nemo(array):
    t0 = time.time()
    for i in range(0,len(array)):
        if array[i] == 'nemo':
            print("Found Nemo!!")
            break
    t1 = time.time()
    print(f'The search took {t1-t0} seconds.')
find_nemo(nemo)
find_nemo(everyone)
find_nemo(large)


# def funchallenge(input):
#     a = 10 #O(1)
#     a = 50 + 3 #O(1)
#     for i in range(len(input)): #O(n)
#         anotherFunction(); #0(n)
#         stranger = True #0(n)
#         a += 1 #0(n)
#     return a #O(1)

# calculation = 3 + 4n
# BIG O(3 + 4n)

#the function simplifies into BIG O(n)

# funchallenge(nemo)
# funchallenge(everyone)
# funchallenge(large)

#Total running time of the funchallenge function =
#O(1 + 1 + n + n*1 + n*1 + n*1 + 1) = O(3n +3) = O(3(n+1))
#Any constant in the Big-O representation can be replaced by 1, as it doesn't really matter what constant it is.
#Therefore, O(3(n+1)) becomes O(n+1)
#Similarly, any constant number added or subtracted to n or multiplied or divided by n can also be safely written as just n
#This is because the constant that operates upon n, doesn't depend on n, i.e., the input size
#Therefore, the funchallenge function can be said to be of O(n) or Linear Time Complexity.