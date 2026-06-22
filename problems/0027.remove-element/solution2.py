"""27. Remove Element

Uses two pointers from both ends: `left` scans for a `val` to drop, `right` scans
from the back for a non-`val` value to move into its place, until the pointers
meet.  This takes O(n) time and O(1) space.
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """Remove every `val` from `nums` in place and return the new length."""

        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] != val:
                left += 1
            # `nums[left]` is a `val` to drop; find a non-`val` from the right.
            while left <= right and nums[right] == val:
                right -= 1
            # `nums[right]` is a non-`val`; move it into the hole at `left`.
            if left < right:
                nums[left] = nums[right]
                left += 1
                right -= 1

        # `nums[:right + 1]` now holds exactly the non-`val` elements.
        return right + 1


if __name__ == "__main__":
    sol = Solution()
    for nums, val in [
        ([3, 2, 2, 3], 3),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2),
        ([], 0),
        ([27], 27),
        ([42, 42, 42], 42),
    ]:
        print(f"nums = {nums}, val = {val} -> ", end="")
        k = sol.removeElement(nums, val)
        print(f"{nums[:k]} (k = {k})")
