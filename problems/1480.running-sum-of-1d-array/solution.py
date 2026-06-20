"""1480. Running Sum of 1d Array

Builds the prefix sums: each output value is the sum of all elements up to and
including that position.  This takes O(n) time and O(n) space.
"""

from itertools import accumulate


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        """Return the running sum of `nums` (each element is the sum so far)."""

        return list(accumulate(nums))


if __name__ == "__main__":
    sol = Solution()
    for nums in [
        [1, 2, 3, 4],
        [1, 1, 1, 1, 1],
        [3, 1, 2, 10, 1],
        [],
    ]:
        print(f"{nums} -> {sol.runningSum(nums)}")
