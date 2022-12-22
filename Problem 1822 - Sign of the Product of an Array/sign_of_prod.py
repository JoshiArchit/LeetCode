import math


class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if 0 in nums:
            return 0
        elif math.prod(nums) > 0:
            return 1
        else:
            return -1


o = Solution()
nums = [1, 5, 0, 2, -3]
print(o.arraySign(nums))
