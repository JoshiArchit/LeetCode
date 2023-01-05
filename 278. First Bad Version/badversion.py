"""
Filename :  badversion.py
Author :    Archit Joshi
Description :   Leetcode problem 278 - First Bad Version
Language :  Python3
Version :   v1.0
Revisions :
v1.0 - First attempt
"""


def firstBadVersion(n: int) -> int:
    """
    Function to return the first bad version from the n total versions
    produced.

    :param n: Total items produced
    :return: First bad version
    """
    left = 1
    right = n

    # Binary search
    while left < right:
        mid = (left + right) // 2

        if isBadVersion(mid):
            # This could be the first bad version or subsequent ones, but we
            # can discard remaining numbers on right
            right = mid
        else:
            # Everything on the left is good, we can discard it
            left = mid + 1

    return left


# Ignore this piece of code below, incomplete stub to drive program for testing
def isBadVersion(version) -> bool:
    if version == bad:
        return True


ip = 5
bad = 4
print(firstBadVersion(ip))
