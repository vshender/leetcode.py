"""977. Squares of a Sorted Array

Uses two pointers.  The input is sorted, so the smallest squares come from the
values closest to zero.  These values sit at the border between the negative and
the non-negative numbers.  One pointer moves left over the negatives, the other
moves right over the non-negatives, and the smaller square is written first.
This takes O(n) time and O(n) space.
"""

import sys


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """Return the squares of `nums` sorted in non-decreasing order."""

        n = len(nums)
        result = [0] * n

        # `pos_idx` is the first non-negative element, `neg_idx` the last
        # negative one --- the two values closest to zero.
        pos_idx = 0
        while pos_idx < n and nums[pos_idx] < 0:
            pos_idx += 1
        neg_idx = pos_idx - 1

        # Merge outward from the split, smaller square first.  An exhausted side
        # yields the `sys.maxsize` sentinel, so the other side is always chosen.
        write_idx = 0
        while neg_idx >= 0 or pos_idx < n:
            neg = nums[neg_idx] if neg_idx >= 0 else sys.maxsize
            pos = nums[pos_idx] if pos_idx < n else sys.maxsize
            if abs(neg) < abs(pos):
                result[write_idx] = neg * neg
                neg_idx -= 1
            else:
                result[write_idx] = pos * pos
                pos_idx += 1
            write_idx += 1

        return result


if __name__ == "__main__":
    sol = Solution()
    for nums in [
        [-4, -1, 0, 3, 10],
        [-7, -3, 2, 3, 11],
        [],
    ]:
        print(f"{nums} -> {sol.sortedSquares(nums)}")
