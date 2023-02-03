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