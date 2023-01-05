"""
Filename :  fibonacci.py
Author :    Archit Joshi
Description :   LeetCode Problem 509 - Fibonacci
Language :  Python3
Version :   v1.0
Revisions :
v1.0 - Using tail recursion

"""


def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2)+fib(n-1)


n = 4
print(fib(4))
