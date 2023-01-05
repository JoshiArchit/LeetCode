"""
Filename :  binarysearch.py
Author :    Archit Joshi
Description :   Leetcode problem 704 - Binary Search
Language :  Python3
Version :   v1.0
Revisions :
v1.0 - Outline of the basic binary search algorithm - SUBMITTED (Generic)
"""


def search(nums: list[int], target: int) -> int:
    return __search(nums, target, left=0, right=len(nums) - 1)


def __search(nums: list[int], target: int, left: int, right: int) -> int:
    # left has crossed over to right, element not found
    # if left > right:
    #     return -1
    while left <= right:

        # Element found in middle
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if target < nums[mid]:
            # Only search left half recursively
            return __search(nums, target, left, mid - 1)
        else:
            # Only search right half recursively
            return __search(nums, target, mid + 1, right)

    return -1


ip = [-1, 0, 3, 5, 9, 12]
find = 9
print(search(ip, find))
