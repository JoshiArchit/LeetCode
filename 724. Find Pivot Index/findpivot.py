"""
Filename :  findpivot.py
Author :  Archit Joshi
Description :   Leetcode problem 724 - Find Pivot Index
Language :  Python3
Version :   v1.0
Revisions :
v1.0 - Initial approach
v1.1 - Removed extra variables to improve space complexity.
v1.2 - Alternate approach to counter time complexity and time limit exceeded
       exception. - SUBMITTED
"""


# #   v1.0, 1.1 - Initial approach (Time limit exceeded in LeetCode console).
# #   Probably because we are calculating sum in each iteration. Correct but not
# #   acceptable. Will work for small inputs ONLY.
# def pivotIndex(nums: list[int]) -> int:
#     for i in range(len(nums)):
#         if sum(nums[:i:]) == sum(nums[i+1::]):
#             return i
#     return -1

#   v1.2 - Alternate approach by reducing sums - WORKING
def pivotIndex(nums: list[int]) -> int:
    left_sum = 0
    total = sum(nums)

    for i in range(len(nums)):
        if left_sum == (total-left_sum-nums[i]):
            return i
        # correctly keep track of left sum at an index
        left_sum += nums[i]
    return -1


ip = [-1, -1, -1, 0, 1, 1]
print(pivotIndex(ip))
