# O(LOG N)

def binarySearch(nums, target):
    low = 0
    high = len(nums)-1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
    return -1


nums = [1, 3, 5, 8, 12, 18]
target = 12

ans = (binarySearch(nums, target))
print(ans)
