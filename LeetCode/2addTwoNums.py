# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
#         print(l2.val, l2.next.val, l2.next.next.val)
#         print(l1.val, l1.next.val, l1.next.next.val)

#         count = 0
#         l1itr = l1
#         str1 = ""
#         while l1itr:
#             str1+=str(l1itr.val)
#             l1itr = l1itr.next
#         str1 = int(str1[::-1])
#         #print(str1)

#         str2 = ""
#         while l2:
#             str2+=str(l2.val)
#             l2 = l2.next
#         str2 = int(str2[::-1])
#         #print(str2)

#         ansArr = int(str(str1 + str2)[::-1])
#         # print(ansArr)
#         # print(type(ansArr))
#         ansArr = [int(d) for d in str(ansArr)]
#         print(ansArr)

        dummy = ListNode()  # creating a resulting linked-list
        cur = dummy  # current pointer..

        carry = 0  # carry, initialize 0

        # either of them have a digit
        while l1 or l2 or carry:

            v1 = l1.val if l1 else 0  # getting digits of v1 only if l1 is not null, else set to 0
            v2 = l2.val if l2 else 0  # getting digits of v1 only if l1 is not null, else set to 0

            # new digit
            val = v1 + v2 + carry
            # if val 15, we have to get the carry out of that
            # can be 1th which represents 10, 2th which represents 20 and so on ...
            carry = val // 10

            val = val % 10  # the left over value gotten from dividing

            # insert it into our list,
            cur.next = ListNode(val)

            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
