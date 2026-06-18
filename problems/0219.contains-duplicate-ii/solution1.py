"""219. Contains Duplicate II

Scans the list once, keeping the last index where each value was seen in a
dictionary.  When a value repeats, only its most recent earlier index can be
within `k`, so a single lookup settles it.  This takes O(n) time and O(n) space.
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """Check whether the array has two equal values at most `k` indices apart."""

        last_occurrence_idx: dict[int, int] = {}

        for i, num in enumerate(nums):
            # Only the most recent earlier index matters: it is the closest, so
            # if any past copy is within `k`, this one is too.
            if num in last_occurrence_idx and i - last_occurrence_idx[num] <= k:
                return True
            last_occurrence_idx[num] = i

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
