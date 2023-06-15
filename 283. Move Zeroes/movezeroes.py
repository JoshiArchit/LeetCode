"""
Filename :  movezeroes.py
Author :    Archit Joshi
Description :   LeetCode problem 283 - Move Zeroes
Language :  Python3
Revisions :
v1.0 - Brute force initial attempt.
v1.1 - Better time complexity.
"""


# v1.0 O(n^2) time complexity
# def moveZeroes(nums: list[int]) -> None:
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             nums.remove(nums[i])
#             nums.append(0)
#     print(nums)

# v1.1
def moveZeroes(nums: list[int]) -> None:
    nonzeroAt = 0

    # Move all non zero elements to start
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nonzeroAt] = nums[i]
            nonzeroAt += 1

    # Populate rest of the list with 0s
    for i in range(nonzeroAt,len(nums)):
        nums[i] = 0

    print(nums)


ip = [0, 1, 0, 3, 12]
moveZeroes(ip)
