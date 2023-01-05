"""
Filename :  isostrings.py
Author :    Archit Joshi
Description :   Leetcode problem 205 - Isomorphic Strings
Language :  Python3
Version :   v1.0
Revisions :
v1.0 - Basic idea and initial approach
"""


def isIsomorphic(s: str, t: str) -> bool:
    dict_1 = {}
    dict_2 = {}

    for c1, c2 in zip(s, t):
        # No mapping exists
        if (c1 not in dict_1) and (c2 not in dict_2):
            dict_1[c1] = c2
            dict_2[c2] = c1
        # Incorrect mapping or second mapping is trying to occur
        elif dict_1.get(c1) != c2 or dict_2.get(c2) != c1:
            return False
    return True


s1 = "badc"
s2 = "baba"
print(isIsomorphic(s1, s2))
