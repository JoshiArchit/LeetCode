"""
Filename :  rotatearray.py
Author :    Archit Joshi
Description :   Leetcode problem 189 - Rotate Array
Language :  Python3
Revisions :
v1.0 - Initial attempt. Brute Force
"""


def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(0, k):
        for j in range(0,len(nums),-1):
            print(j)


a = [1, 2, 3, 4, 5, 6, 7]
b = 3
rotate(a, b)
# Should become - [5,6,7,1,2,3,4]
