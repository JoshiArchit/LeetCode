class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff1 = -1
        diff2 = -1

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                # Get index of first difference
                if diff1 == -1:
                    diff1 = i
                # Get index of second difference
                elif diff2 == -1:
                    diff2 = i
                else:
                    # More than 2 differences , swap impossible
                    return False

        # Check if swap possible
        return s1[diff1] == s2[diff2] and s1[diff2] == s2[diff1]

o = Solution()
s1 = "yhy"
s2 = "hyc"
print(o.areAlmostEqual(s1, s2))