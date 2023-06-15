def findTheDifference(s: str, t: str) -> str:
    # Use XOR to compare each character in string and return result
    char = 0

    for c in s:
        char ^= ord(c)

    for c in t:
        char ^= ord(c)

    return chr(char)


str1 = "abcd"
str2 = "abcde"

print(findTheDifference(str1, str2))
