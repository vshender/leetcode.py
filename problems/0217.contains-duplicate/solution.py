"""217. Contains Duplicate

Scans the list once, keeping the values seen so far in a set.  A value that is
already in the set means a duplicate exists, so the scan can stop early.  This
takes O(n) time and O(n) space.
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """Check whether the array contains any duplicate value."""

        seen: set[int] = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False


if __name__ == "__main__":
    sol = Solution()
    for nums in [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
        [],
    ]:
        print(f"{nums} -> {sol.containsDuplicate(nums)}")
