"""977. Squares of a Sorted Array

Uses the two-pointer technique from both ends of the sorted input.  Since the
array runs from the most negative to the most positive value, the largest square
is always at one of the two ends.  The larger end is squared and written to the
back of the result, and that pointer steps inward, so the result fills from back
to front in order.  This takes O(n) time and O(n) space.
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """Return the squares of `nums` sorted in non-decreasing order."""

        n = len(nums)
        result = [0] * n

        left, right = 0, n - 1
        # Fill `result` from the back, placing the larger end square each step.
        for write_idx in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[write_idx] = nums[left] * nums[left]
                left += 1
            else:
                result[write_idx] = nums[right] * nums[right]
                right -= 1

        return result


if __name__ == "__main__":
    sol = Solution()
    for nums in [
        [-4, -1, 0, 3, 10],
        [-7, -3, 2, 3, 11],
        [],
    ]:
        print(f"{nums} -> {sol.sortedSquares(nums)}")
