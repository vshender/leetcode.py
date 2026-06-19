"""169. Majority Element

Counts how often each value appears with a hash map and returns a value as soon
as its count passes half the length.  The problem guarantees such a value exists.
This takes O(n) time and O(n) space.
"""

from collections import defaultdict


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """Return the majority element of `nums` (the value appearing more than n/2 times)."""

        threshold = len(nums) / 2
        counts: defaultdict[int, int] = defaultdict(int)

        for num in nums:
            counts[num] += 1
            if counts[num] > threshold:
                return num

        assert False, "nums always has a majority element"


if __name__ == "__main__":
    sol = Solution()
    for nums in [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2],
    ]:
        print(f"{nums} -> {sol.majorityElement(nums)}")
