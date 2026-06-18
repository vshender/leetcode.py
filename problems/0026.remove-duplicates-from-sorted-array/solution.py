"""26. Remove Duplicates from Sorted Array

Uses the two-pointer technique in place.  A write pointer marks the end of the
unique prefix while a read pointer scans ahead; each value that differs from the
last unique one is written just after it.  The array is sorted, so equal values
are always adjacent and a single comparison is enough.  This takes O(n) time and
O(1) space.
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """Remove duplicates in place and return the count of unique elements."""

        if not nums:
            return 0

        last_unique = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[last_unique]:
                last_unique += 1
                nums[last_unique] = nums[i]

        return last_unique + 1


if __name__ == "__main__":
    sol = Solution()
    for nums in [
        [],
        [1],
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
    ]:
        print(f"{nums} -> ", end="")
        k = sol.removeDuplicates(nums)
        print(f"k = {k}, {nums[:k]}")
