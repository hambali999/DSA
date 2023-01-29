# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        #Input: strs = ["flower","flow","flight"]
        #Output: "fl"

        res = ""

        # first string => 0,1,2,3,4,5, => strs[0] == flower
        for i in range(len(strs[0])):
            print(i)
            for s in strs:
                # check if every single str at index i is the same
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
        # what if goes out of bounds
