"""27. Remove Element

Scans the list once with a write pointer: every value that is not `val` is copied
to the next write slot, compacting the kept elements to the front in order.  This
takes O(n) time and O(1) space.
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """Remove every `val` from `nums` in place and return the new length."""

        # `write_idx` is the next slot for a kept element.
        write_idx = 0
        for read_idx in range(len(nums)):
            if nums[read_idx] != val:
                nums[write_idx] = nums[read_idx]
                write_idx += 1

        return write_idx


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
