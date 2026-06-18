"""219. Contains Duplicate II

Slides a window of the last `k` values across the list, holding them in a set.
Before adding each value it checks the window: if the value is already there,
an equal value sits within `k` indices.  The set never holds two equal values,
because such a pair would be caught at the check before the second one is added.
This takes O(n) time and O(min(n, k)) space.
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """Check whether the array has two equal values at most `k` indices apart."""

        seen_in_window: set[int] = set()

        for i, num in enumerate(nums):
            if num in seen_in_window:
                return True

            # Add the current value, then drop the one that just left the window
            # of size `k`.  Adding before removing also keeps `k == 0` correct:
            # the value is removed on the same step, so the window stays empty.
            seen_in_window.add(num)
            if i >= k:
                seen_in_window.remove(nums[i - k])

        return False


if __name__ == "__main__":
    sol = Solution()
    for nums, k in [
        ([1, 2, 3, 1], 3),
        ([1, 0, 1, 1], 1),
        ([1, 2, 3, 1, 2, 3], 2),
        ([1, 2, 3], 0),
    ]:
        print(f"nums = {nums}, k = {k} -> {sol.containsNearbyDuplicate(nums, k)}")
