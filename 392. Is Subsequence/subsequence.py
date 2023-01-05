"""
Filename :  subsequence.py
Author :    Archit Joshi
Description :   Leetcode Problem 392
Language :  Python3
Revisions :
v1.0 - First attempt. Iterative approach.
Time Complexity : O(T), T = length of target string
Space Complexity : O(1)
v1.1 - Using all() function -- NEW
"""


def isSubsequence(s: str, t: str) -> bool:
    # c1, c2 = 0,0
    # while c1 < len(s) and c2 < len(t):
    #     if s[c1] == t[c2]:
    #         c1 += 1
    #     c2 += 1
    #
    # return c1 == len(s)

    # lazy loading using iter()
    t = iter(t)
    return all(c in t for c in s)



s = "acb"
t = "ahbgdc"
print(isSubsequence(s, t))
