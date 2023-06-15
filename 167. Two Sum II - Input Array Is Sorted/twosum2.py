"""
Filename :  twosum2.py
Author :    Archit Joshi
Description :   LeetCode Problem 167 - Two Sum II
Language :  Python3
Revisions :
v1.0 - First attempt. Brute force borrowed from Problem 1 : Two Sums
v1.1 - Using the property of a sorted array
"""


# # v1.0
# def twoSum(numbers: list[int], target: int) -> list[int]:
#     hashmap = {}
#
#     for i in range(len(numbers)):
#         # Found a match return
#         if target - numbers[i] in hashmap:
#             return [hashmap[target - numbers[i]] + 1, i + 1]
#         else:
#             hashmap[numbers[i]] = i

def twoSum(numbers: list[int], target: int) -> list[int]:
    low = 0
    high = len(numbers) - 1

    while low < high:
        if numbers[low] + numbers[high] == target:
            return [low + 1, high + 1]
        elif numbers[low] + numbers[high] < target:
            low += 1
        else:
            high -= 1


ip = [2, 3, 4]
op = 6
print(twoSum(ip, op))
