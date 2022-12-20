class Solution(object):

    # Brute Force
    def countOddsBrute(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        count = 0
        for num in range(low, high + 1):
            if num % 2 != 0:
                count += 1

        return count

    # Optimised
    def countOdds(self, low, high):
        """
            :type low: int
            :type high: int
            :rtype: int
        """
        if low % 2 == 0:
            return (high - low + 1) // 2
        return ((high - low) // 2) + 1


s = Solution()
print(s.countOdds(2, 7))
