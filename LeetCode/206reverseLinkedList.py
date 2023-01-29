# https://leetcode.com/problems/reverse-linked-list/submissions/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head

        # T O(N), M O(1)
        while curr:
            nxt = curr.next  # current node's next
            curr.next = prev  # current node next's point back to prev
            prev = curr  # previous node now points to this current node
            curr = nxt  # 1st line
        return prev
