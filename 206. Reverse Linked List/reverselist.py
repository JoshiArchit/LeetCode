"""
Filename :  reverselist.py
Author :    Archit Joshi
Description :   LeetCode Problem 206 - Reverse Linked List
Language :  Python3
Revisions :
v1.0 - Iterative Attempt
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (head.next is None):
            return head
        # Go to list node and start building new list in place
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return node


    def printList(self,l1):
        output = ""
        while l1:
            output += f"{l1.val} -> "
            l1 = l1.next
        output += "None"
        return output


l1 = ListNode(1, ListNode(2, ListNode(3)))
s = Solution()
print(s.printList(s.reverseList(l1)))
