def main(arr):

    arr = sorted(arr)

    sum = 0
    checker = []

    for x in arr:
        # print(x)
        if x not in checker:
            if x > 0:
                sum+=x
                checker.append(x)


    # print("=")
    # print(checker)
    print(sum)

# main([1,2,1,4,1])
# main([1,2,-1,3,4,10,10,-10,-1])


def maximumSubarraySum(arr):
       n = len(arr)
       maxSum = 0
       currSum = 0

       for i in range(0, n):
           currSum = currSum + arr[i]
           print(currSum)
           if(currSum > maxSum):
               maxSum = currSum
           if(currSum < 0):
               currSum = 0
      
       return maxSum

if __name__ == "__main__":
    # Your code goes here
    print(maximumSubarraySum([1,2,-1,3,4,10,10,-10,-1]));
