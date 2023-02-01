
#O(N^2)
def getPairsCount(arr, sum):
      
    count = 0  # Initialize result

    n = len(arr)
  
    # Consider all possible pairs
    # and check their sums
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                print(arr[i], arr[j])
                count += 1
    
    return count
  
  
# Driver function
arr = [1, 5, 7, -1, 5]
sum = 6
print("Count of pairs is", getPairsCount(arr, sum))


def pair_sum(arr,k):
    
    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()
    
    # For every number in array
    for num in arr:
        
        # Set target difference
        target = k-num
        
        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        
        else:
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )
    
    
    # FOR TESTING
    print(output)
    return len(output)

arr = [1, 5, 7, -1, 5]
sum = 6
print("Count of pairs is", pair_sum(arr, sum))