# The total_length variable is used to keep track of the total length of the non-overlapping intervals. 
# The current_start and current_end variables keep track of the current interval being processed. 

# If the start of the next interval is less than or equal to the end of the current interval, 
# then they overlap and the current_end variable is updated to be the maximum of the two ends. 

# If they do not overlap, then the length of the current interval 
# is added to the total_length and the current_start and current_end variables are updated to be the start and end of the next interval.

def sum_of_intervals(intervals):
    #     print(intervals)
#     intervals.sort(key=lambda x: x[0])
    intervals = sorted(intervals)
    print(intervals)
    total_length = 0
    current_start, current_end = intervals[0]
    for start, end in intervals[1:]:
        print(start,end)
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            total_length += current_end - current_start
            current_start, current_end = start, end
    total_length += current_end - current_start
    return total_length


# test cases
# sumIntervals( [
#    [1,2],
#    [6, 10],
#    [11, 15]
# ] ) => 9

# sumIntervals( [
#    [1,4],
#    [7, 10],
#    [3, 5]
# ] ) => 7
        
        
