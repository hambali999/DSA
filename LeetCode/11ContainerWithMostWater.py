class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # brute force O(N*N)
        # print(height)

        # res = 0

        # for l in range(len(height)):
        #     for r in range(l+1, len(height)):
        #         area = (r-l) * min(height[l], height[r])
        #         res = max(res, area) #everytime check res or area computed is higher

        # return res

        # linear time O(log N)

        print(height)

        res = 0
        l, r = 0, len(height)-1

        while l < r:
            # right-left = breadth, min of both heights
            area = (r-l) * min(height[l], height[r])
            # everytime check res or area computed is higher
            res = max(res, area)

            if height[l] < height[r]:
                l += 1  # shift left pointer to the right
            elif height[r] < height[l]:
                r -= 1  # shift right pointer to the left
            else:
                r -= 1  # can do this too l +=

        return res
