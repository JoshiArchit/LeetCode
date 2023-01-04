"""
Filename :  runningsum.py
Author :    Archit Joshi
Description :   Leetcode problem 1480 - Running sum of 1d array solution
Language :  Python3
Version :   v1.0
Revisions :
v1.0 - Outlined logic and first attempt. All test cases passed.
       Beats 25.34% runtime, 26.68% memory
"""


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        output = [nums[0]]
        for i in range(1, len(nums)):
            output.append(nums[i] + output[i - 1])
        return output


s = Solution()
ip = [3, 1, 2, 10, 1]
print(s.runningSum(ip))
