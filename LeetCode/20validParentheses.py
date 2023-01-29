# https://leetcode.com/problems/valid-parentheses/submissions/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closeToOpen = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in closeToOpen:  # ), }, ]
                # if stack is not empty, and stack last appended
                # stack[-1] represents the last value in the stack
                # ch == ), }, ],
                # closeToOpen[')'] =>  (
                # closeToOpen['}'] =>  {
                # closeToOpen[']'] =>  [

                if stack and stack[-1] == closeToOpen[ch]:
                    stack.pop()  # pop the last appended stack
                else:
                    return False
            else:  # (, {, [
                stack.append(ch)
        if stack == []:
            return True
        else:
            return False


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
