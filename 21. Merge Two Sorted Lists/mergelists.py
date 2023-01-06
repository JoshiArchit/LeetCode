"""
Filename :  mergelists.py
Author :    Archit Joshi
Description :   LeetCode Problem 21 - Merge Two Sorted Lists
Language :  Python3
Revisions :
v1.0 - First attempt.
v1.1 - Added stubs to test code - class ListNode, function print to print list
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Solution to merge two linked lists in ascending order
    """
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted lists in a new sorted list.

        :param list1: Sorted linked list 1
        :param list2: Sorted linked list 2
        :return: Pointer to the merged sorted link list
        """
        head = ListNode()
        node = head

        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        # Append non-exhausted list at the end
        if list1:
            node.next = list1
        else:
            node.next = list2

        # return the node ahead of head
        return head.next

    # Driver function to test code
    def printList(self, l1: ListNode):
        output = ""
        while l1:
            output += f"{l1.val} -> "
            l1 = l1.next
        output += "None"
        return output


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

s = Solution()

print(s.printList(s.mergeTwoLists(list1, list2)))
