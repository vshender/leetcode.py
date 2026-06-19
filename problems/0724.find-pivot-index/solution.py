"""724. Find Pivot Index

Sweeps left to right keeping the running sum of the elements to the left of the
current index; the right sum is then the total minus the left sum minus the
current value.  Returns the first index where the left and right sums are equal.
This takes O(n) time and O(1) space.
"""


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        """Return the leftmost pivot index of `nums`, or -1 if there is none."""

        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]
            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1


if __name__ == "__main__":
    sol = Solution()
    for nums in [
        [1, 7, 3, 6, 5, 6],
        [1, 2, 3],
        [2, 1, -1],
        [0],
        [1],
        [1, 1],
    ]:
        print(f"{nums} -> {sol.pivotIndex(nums)}")
