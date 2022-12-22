class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """

        s = 0
        p = 1
        while n:
            num = n % 10
            p *= num
            s += num
            n = n//10

        return p-s


o = Solution()
n = 4421
print(o.subtractProductAndSum(n))
