class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort and rearrange nums in descending order
        sorted_nums = sorted(nums)[::-1]
        for i in range(len(sorted_nums) - 2):
            # for a triangle, sum of two sides cannot be smaller than its third side
            if sorted_nums[i] < sorted_nums[i+1] + sorted_nums[i+2]:
                return sorted_nums[i] + sorted_nums[i + 1] + sorted_nums[i+2]
        return 0


o = Solution()
nums = [3, 2, 3, 4]
print(o.largestPerimeter(nums))
