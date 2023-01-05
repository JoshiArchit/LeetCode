"""
Filename :  containsduplicates.py
Author :    Archit Joshi
Description :   LeetCode Problem 217 - Contains Duplicates
Language :  Python3
Version :   v1.0
Revisions :
v1.0 - Initial attempt using sets and hashmaps
v1.1 - Added another solution but with less efficient space complexity

"""


def containsDuplicate(nums: list[int]) -> bool:
    hashmap = set()
    for item in nums:
        if item in hashmap:
            return True
        else:
            hashmap.add(item)
    return False


# # v1.1 - We add everything to set.
# def containsDuplicate(nums: list[int]) -> bool:
# return len(nums) != len(set(nums))

ip = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicate(ip))
