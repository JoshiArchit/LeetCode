class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """

        smallest = -1
        count = 0
        index = -1
        # Get valid set of points
        for item in points:
            if item[0] == x or item[1] == y:
                # This is a valid point, calculate manhattan dist
                manhattan = abs(x - item[0]) + abs(y - item[1])
                # If it is the smallest or if current smallest is out of bounds
                if manhattan < smallest or smallest == -1:
                    smallest = manhattan
                    index = count
            count += 1
        return index


o = Solution()
x = 3
y = 4
points = [[2,3]]
print(o.nearestValidPoint(x, y, points))
