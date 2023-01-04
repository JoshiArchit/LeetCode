"""
Filename :  runningsum.py
Author :    Archit Joshi
Description :   Leetcode problem 1480 - Running sum of 1d array solution
Language :  Python3
Version :   v1.0
Revisions :
v1.0 - Outlined logic and first attempt. All test cases passed.
       Beats 25.34% runtime, 26.68% memory
v1.1 - Second attempt without using a new list - SUBMITTED.
v1.2 - Third attempt, with a fewer number of iterations inside the loop.
"""


class Solution:
    #   #v1.0 - First attempt
    # def runningSum(self, nums: list[int]) -> list[int]:
    #     output = [nums[0]]
    #     for i in range(1, len(nums)):
    #         output.append(nums[i] + output[i - 1])
    #     return output

    #   v1.1 - Second attempt without a new list - SUBMITTED
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            nums[i+1] += nums[i]
        return nums

    # # v1.2 - Third attempt with similar approach. Runs the loop len(nums)-1
    # # times. Adopted from v1.0 and v1.1 (slower????)
    # def runningSum(selfself, nums: list[int]) -> list[int]:
    #     for i in range(1,len(nums)):
    #         nums[i] += nums[i-1]
    #     return nums



s = Solution()
ip = [1,2,3,4]
print(s.runningSum(ip))
