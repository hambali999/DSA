class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        newArray = []

        for i in range(len(nums)):
            # 1st loop = [0:3]
            # 2nd loop = [1:4]
            # 3rd loop = [2:5]
            # continue ...
            if len(nums[i:k+i]) == k:
                newArray.append(max(nums[i:k+i]))
        return (newArray)
