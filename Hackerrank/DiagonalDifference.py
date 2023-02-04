def diagonalDifference(arr):
    # Write your code here
    leftdiagonal = []
    rightdiagonal = []

    matrixtype = len(arr)
    
    for x,y in enumerate(arr):
        leftdiagonal.append(y[x])
    for x,y in enumerate(arr[::-1]):
        rightdiagonal.append(y[x])
    sumleftdiagonal = sum(leftdiagonal)
    sumrightdiagonal = sum(rightdiagonal)
    return(max(sumleftdiagonal,sumrightdiagonal)-min(sumleftdiagonal,sumrightdiagonal))

#refactored
def test(arr):
    # Write your code here
    sumleftdiagonal = 0
    sumrightdiagonal = 0
    
    for x,y in enumerate(arr):
        sumleftdiagonal+=y[x]
    for x,y in enumerate(arr[::-1]):
        sumrightdiagonal+=y[x]

    return(max(sumleftdiagonal,sumrightdiagonal)-min(sumleftdiagonal,sumrightdiagonal))

a = [[ 1, 2, 3, 4 ],
     [ 5, 3, 2, 8 ],
     [ 1, 2, 3, 4 ],
     [ 5, 6, 7, 3 ]]

print(test(a))
# print(max([1,3,4,5,2,10,12,15,2]))