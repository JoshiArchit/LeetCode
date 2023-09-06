"""
Filename : anagram.py
Author : Archit Joshi
Description : Leetcode problem 242 - Anagram
Language : python3
"""


def isAnagram(text1, text2):
    if len(text1) != len(text2):
        return False

    hash_table = dict()

    for i in range(len(text1)):
        if text1[i] in hash_table:
            hash_table[text1[i]] += 1
        else:
            hash_table[text1[i]] = 1

    for i in range(len(text2)):
        if text2[i] in hash_table:
            hash_table[text1[i]] -= 1

    print(hash_table)

    if all(value == 0 for value in hash_table.values()):
        return True
    return False


def main():
    s = "a"
    t = "ab"

    print(isAnagram(s, t))


if __name__ == "__main__":
    main()
