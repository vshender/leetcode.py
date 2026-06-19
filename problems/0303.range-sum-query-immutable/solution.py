"""303. Range Sum Query - Immutable

Precomputes inclusive prefix sums once, so any range sum is the difference of two
of them: the sum of `nums[left..right]` is the prefix sum up to `right` minus the
prefix sum just before `left`.  This takes O(n) preprocessing time, O(1) per
query, and O(n) space.
"""

from itertools import accumulate


class NumArray:
    def __init__(self, nums: list[int]) -> None:
        """Precompute the inclusive prefix sums of `nums`."""

        self.prefix_sums: list[int] = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        """Return the sum of `nums[left..right]`, inclusive."""

        # Everything up to `right`, minus everything before `left`.
        prefix_before_left = self.prefix_sums[left - 1] if left > 0 else 0
        return self.prefix_sums[right] - prefix_before_left


if __name__ == "__main__":
    for array, ranges in [
        (
            [-2, 0, 3, -5, 2, -1],
            [[0, 2], [2, 5], [0, 5], [1, 2], [1, 1]],
        ),
    ]:
        print(f"NumArray: {array}")
        obj = NumArray(array)
        for left, right in ranges:
            print(f"  sumRange: [{left}, {right}] -> {obj.sumRange(left, right)}")
