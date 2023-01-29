# https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # BRUTE FOR METHOD O(N*2)
        # for i in range(len(nums)):
        #     for x in range(len(nums)):
        #         if i != x:
        #             if nums[i] + nums[x] == target:
        #                 return [i, x]

        # HASHMAP METHOD O(N)
        prevMap = {}  # val : index
        for i, n in enumerate(nums):  # index, #value
            print(i, n)
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

        # numdict = {}

        # for i, v in enumerate(nums):
        #     print(i,v)
        #     diff = target - v
        #     if diff in numdict:
        #         return [numdict[diff], i]
        #     else:
        #         numdict[v] = i
        # return

        # chkMap = {}
        # for i, n in enumerate(nums): #index, value
        #     print(i,n)
        #     diff = target - n
        #     if diff in chkMap:
        #         return [chkMap[diff], i]
        #     chkMap[n] = i
        # return


# https://leetcode.com/problems/two-sum/
