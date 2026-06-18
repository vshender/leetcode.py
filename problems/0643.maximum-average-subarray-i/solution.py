"""643. Maximum Average Subarray I

Uses a fixed-size sliding window of length `k`.  It sums the first window, then
slides one step at a time, subtracting the value that leaves and adding the one
that enters, so each step is O(1).  Since `k` is fixed, the largest window sum
gives the largest average, so it tracks the max sum and divides once at the end.
This takes O(n) time and O(1) space.
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """Return the maximum average of any contiguous subarray of length `k`."""

        window_sum = 0
        for i in range(k):
            window_sum += nums[i]

        max_window_sum = window_sum
        for i in range(k, len(nums)):
            # Slide the window: drop the element leaving, add the one entering.
            window_sum += nums[i] - nums[i - k]
            max_window_sum = max(max_window_sum, window_sum)

        return max_window_sum / k


if __name__ == "__main__":
    sol = Solution()
    for nums, k in [
        ([1, 12, -5, -6, 50, 3], 4),
        ([5], 1),
    ]:
        print(f"nums = {nums}, k = {k} -> {sol.findMaxAverage(nums, k)}")
