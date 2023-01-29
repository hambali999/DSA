# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        original_num = x
        reversed_num = 0

        while x > 0:
            # 121 mod 10 = 1, 121 keep dividing by 10,
            last_digit = x % 10

            # remove last digit from num. e.g. lets say num is 121. num is then set to 121 // 10 which is 12
            x = x // 10

            # append last digit to right of rev_num, e.g. 1 becomes 21 after appending 2
            reversed_num = reversed_num*10 + last_digit

            # e.g if x is 121
            # first run => 1
            # second run => 21
            # third run => 121
            print(reversed_num)

        return original_num == reversed_num
