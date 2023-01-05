"""
Filename :  arraysquares.py
Author :    Archit Joshi
Description :   Leetcode problem 977 - Squares of a Sorted Array
Language :  Python3
Revisions :
v1.0 - Initial attempt. Bruteforce
v1.1 - One liner return statement
"""


# # v1.0
# def sortedSquares(nums: list[int]) -> list[int]:
#     # for i in range(len(nums)):
#     #     nums[i] = nums[i] * nums[i]
#
#     return sorted(nums)

def sortedSquares(nums: list[int]) -> list[int]:
    return sorted(num * num for num in nums)


ip = [-4, -1, 0, 3, 10]
print(sortedSquares(ip))
