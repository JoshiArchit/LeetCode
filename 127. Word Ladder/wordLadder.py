"""
Filename : wordLadder
Author :    Archit Joshi
Description :   LeetCode word ladder problem
Language :  Python
Revisions :
"""
from collections import defaultdict, deque


class Solution:

    def findPath(self):
        file = "D:\Projects\LeetCode\dict..txt"
        start = "harp"
        end = "ramp"

        if end not in open(file).read():
            return None

        adjacencyList = defaultdict(list)

        with open(file) as f:
            for word in f:
                word = word.strip()
                if len(word) == len(start):
                    for j in range(len(word)):
                        intermediate = word[:j] + "_" + word[j + 1:]
                        adjacencyList[intermediate].append(word)

        # BFS
        predecessor = {start: None}
        q = deque([start])
        while q:
            for i in range(len(q)):
                current = q.popleft()
                if current == end:
                    break
                for j in range(len(current)):
                    intermediate = current[:j] + "_" + current[j + 1:]
                    for neighbor in adjacencyList[intermediate]:
                        if neighbor not in predecessor:
                            predecessor[neighbor] = current
                            q.append(neighbor)

        if end in predecessor:
            trace = []
            current = end
            while current != start:
                trace.insert(0, current)
                current = predecessor[current]
            trace.insert(0, start)
            return trace
        else:
            return None

    def result(self):
        path = self.findPath()
        for item in path:
            print(item)


def main():
    s = Solution()
    s.result()


main()
