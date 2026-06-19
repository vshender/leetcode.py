"""1991. Find the Middle Index in Array

Sweeps left to right keeping the running sum of the elements to the left of the
current index; the right sum is then the total minus the left sum minus the
current value.  Returns the first index where the left and right sums are equal.
This takes O(n) time and O(1) space.
"""


class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        """Return the leftmost middle index of `nums`, or -1 if there is none."""

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
        [2, 3, -1, 8, 4],
        [1, -1, 4],
        [2, 5],
        [0],
        [1],
        [1, 1],
    ]:
        print(f"{nums} -> {sol.findMiddleIndex(nums)}")
