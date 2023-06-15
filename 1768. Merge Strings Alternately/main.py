def mergeAlternately(word1: str, word2: str) -> str:
    final_string = ''
    m = len(word1)
    n = len(word2)

    for i in range(max(m, n)):
        if i < m:
            final_string+=word1[i]
        if i < n:
            final_string+=word2[i]
        i += 1
    return final_string

word1 = 'abc'
word2 = 'pqr'
print(mergeAlternately(word1, word2))