"""
Filename :  tribonacci.py
Author :    Archit Joshi
Description :   LeetCode Problem 1137 - Tribonacci number
Language :  Python3
Version :   v1.0
Revisions :
v1.0 - Using classic recursion
v1.1 - Dynamic Programming
"""


# # v1.0 - Wont work due to complexity - 3^N
# def tribonacci(n: int) -> int:
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

def tribonacci(n: int) -> int:
    if n < 3:
        return 1 if n else 0

    x, y, z = 0, 1, 1

    for _ in range(n - 2):
        x, y, z = y, z, x + y + z
    return z


ip = 25
print(tribonacci(ip))
