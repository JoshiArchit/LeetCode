"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

"""


class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """

        # sort the salary list and exclude first and last values from sum
        return float(sum(sorted(salary)[1:-1])) / float(len(salary) - 2)


s = Solution()
# salary = [4000,3000,1000,2000]
salary = [48000, 59000, 99000, 13000, 78000, 45000, 31000, 17000, 39000, 37000,
          93000, 77000, 33000, 28000, 4000, 54000, 67000, 6000, 1000, 11000]
print(s.average(salary))
