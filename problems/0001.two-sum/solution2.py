"""1. Two Sum

Scans the list once, storing each seen value with its index, and for every value
looks up the complement that reaches the target.  This takes O(n) time and O(n)
space.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Return the indices of two numbers that add up to the target."""

        seen = {}

        for idx, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], idx]

            seen[value] = idx

        return []


if __name__ == "__main__":
    nums = [11, 2, 15, 7]
    target = 9

    s = Solution()
    print(s.twoSum(nums, target))
