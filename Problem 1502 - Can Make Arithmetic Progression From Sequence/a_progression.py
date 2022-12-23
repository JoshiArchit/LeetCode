class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        # Getting difference between consecutive elements and inserting in set
        # If the sequence is an AP there should be only 1 element in set
        return len(set(arr[i - 1] - arr[i] for i in range(1, len(arr)))) == 1


o = Solution()
arr = [1, 2, 4]
print(o.canMakeArithmeticProgression(arr))
