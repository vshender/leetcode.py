"""1413. Minimum Value to Get Positive Step by Step Sum

Tracks the lowest running prefix sum while scanning.  The start value must lift
that lowest point to at least 1 (and be positive itself), so the answer is one
more than how far the running sum dips below zero.  This takes O(n) time and
O(1) space.
"""


class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        """Return the smallest positive start value that keeps every running sum at least 1."""

        running_sum = 0
        min_sum = 0
        for num in nums:
            running_sum += num
            min_sum = min(min_sum, running_sum)

        return 1 - min_sum  # min_sum <= 0, so this equals 1 + abs(min_sum)


if __name__ == "__main__":
    sol = Solution()
    for nums in [
        [-3, 2, -3, 4, 2],
        [1, 2],
        [1, -2, -3],
        [],
    ]:
        print(f"{nums} -> {sol.minStartValue(nums)}")
