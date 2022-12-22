"""
filename : addtwonumbers.py
LeetCode problem 2
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carryover = 0
        curr = head = ListNode()

        # Run as long as 1 list has not been traversed to the end
        while l1 or l2:
            # Store the value from carry over in digit
            digit = carryover
            # Both lists are not exhausted
            if l1 and l2:
                digit += (l1.val + l2.val)
                l1 = l1.next
                l2 = l2.next
            # LinkedList 2 has been exhausted
            elif l1:
                digit += l1.val
                l1 = l1.next
            # LinkedList 1 has been exhausted
            elif l2:
                digit += l2.val
                l2 = l2.next
            # Store the first digit from 2 digit sum in carryover
            carryover = digit // 10
            # Create node with only 1st place digit
            curr.next = ListNode(digit % 10)
            # Move ahead
            curr = curr.next

        # If at the end there was any carry over left (has to be a value 1)
        if carryover == 1:
            # Create one last node and store the carryover 1
            curr.next = ListNode(carryover)
            curr = curr.next

        # Return the pointer to the head
        return head.next


