"""
Filename :  rotatearray.py
Author :    Archit Joshi
Description :   Leetcode problem 189 - Rotate Array
Language :  Python3
Revisions :
v1.0 - Initial attempt. Brute Force - SUBMITTED
"""


def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    a = [0] * n
    for i in range(n):
        a[(i + k) % n] = nums[i]

    nums[:] = a

a = [1, 2, 3, 4, 5, 6, 7]
b = 3
rotate(a, b)
# Should become - [5,6,7,1,2,3,4]
