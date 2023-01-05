"""
Filename :  searchposition.py
Author :  Archit Joshi
Description :   LeetCode problem 35 - Search Insert Position
Language :  Python3
Version :   v1.0
Revisions :
v1.0 - First Attempt, using binary search to calculate index

"""


def searchInsert(nums: list[int], target: int) -> int:
    return __searchInsert(nums, target, left=0, right=len(nums) - 1)


def __searchInsert(nums: list[int], target: int, left: int, right: int) -> int:
    # Exit condition
    while left <= right:

        # Calculate mid
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            # Search recursively in left half
            return __searchInsert(nums, target, left, mid - 1)
        else:
            # Search recursively in right half
            return __searchInsert(nums, target, mid + 1, right)

    # Return where the element could be positioned if inserted
    return left


ip = [1, 3, 5, 6]
num = 2
print(searchInsert(ip, num))
