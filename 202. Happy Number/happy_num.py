class Solution:
    def isHappy(self, n: int) -> bool:
        # Hashmap to detect cycles/loops
        seen = set()
        while n!= 1:
            # Use slicing to calculate the sum of squares of each digit
            n = sum([int(i) ** 2 for i in str(n)])
            if n in seen:
                return False
            else:
                seen.add(n)
        return True


o = Solution()
n = 2
print(o.isHappy(n))
