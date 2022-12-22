"""
filename : twosums.py
author : Archit Joshi
language: python3

LeetCode problem 1 - Two Sums
Provisions made to accept user input in console.

"""


class Solution:
    """
    Class to test if a target value can be obtained by summing up two values
    from our list of input numbers. Return the indices of these two input number
    solutions. No duplicates allowed.


    """

    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        """
        Run the algorithm on inputs received based on example -

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

        :param nums: list of numbers
        :param target: target value for sum
        :return: indices of 2 numbers that add to target value

        """
        # Create empty hashmap
        hashMap = {}

        for i in range(len(nums)):
            # check if difference is already there in hashMap
            if target - nums[i] in hashMap:
                # We have found the solution , so return a list of the indices
                return [hashMap[target - nums[i]], i]
            else:
                # It's not there so, i.e. first visit. Add to hashMap
                hashMap[nums[i]] = i


# Function to get input from user
def get_inputs() -> tuple[list[int], int]:
    """
    Accept input of list of numbers and target value from the user.

    :return: list of numbers and target value
    """

    # Empty list of values
    numbers = []
    print("Enter a list of numbers : ")
    # Loop till we get an empty line
    while True:
        val = input()
        # Check for empty line
        if val == "":
            break
        # If value received, convert to int and add to list
        else:
            numbers.append(int(val))

    # Accept and convert the value received for target to an int
    target = int(input("Enter target value : "))

    # Return the inputs received to main()
    return numbers, target


def main() -> None:
    """
    The main function to instantiate class and run algorithm
    :return: None

    """

    # Receive inputs
    numbers, target = get_inputs()

    # Instantiate class and run algorithm
    obj1 = Solution()
    result = obj1.twoSum(numbers, target)

    # If-Else to handle cases if there exists no result
    if result:
        print(f"The indices of the solution numbers are : {result}")
    else:
        print("Result not possible from given values")


if __name__ == "__main__":
    main()
