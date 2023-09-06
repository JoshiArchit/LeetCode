def hash_val(string):
    # Initialize the hash value to 0
    hash_value = 0

    # Sum the ordinal values of all characters in the string
    for char in string:
        hash_value += ord(char)

    return hash_value


def strStr(text, pattern):
    m, n = len(pattern), len(text)
    pattern_hash = hash_val(pattern)
    text_hash = hash_val(text[:m])

    result = []

    for i in range(n-m+1):
        if pattern_hash == text_hash and text[i:i + m] == pattern:
            result.append(i)

        if i < n - m:
            # Recalculate the hash value for the next substring using rolling hash
            text_hash = (text_hash - ord(text[i])) + ord(text[i + m])

    return result


haystack = "hello"
needle = "ll"

print(strStr(haystack, needle))
