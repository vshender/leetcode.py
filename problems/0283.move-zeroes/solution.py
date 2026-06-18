"""283. Move Zeroes

Uses the two-pointer technique in place.  A write pointer packs every non-zero
value toward the front while keeping their order, then the rest of the array is
filled with zeroes.  This takes O(n) time and O(1) space.
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """Move all zeroes to the end of the array in place, keeping the order of the other values."""

        # Pack every non-zero value at the front, in order.
        write_idx = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[write_idx] = nums[cur]
                write_idx += 1

        # Everything from `write_idx` on is leftover; fill it with zeroes.
        for cur in range(write_idx, len(nums)):
            nums[cur] = 0


if __name__ == "__main__":
    sol = Solution()
    for nums in [
        [0, 1, 0, 3, 12],
        [0],
        [],
    ]:
        print(f"{nums} -> ", end="")
        sol.moveZeroes(nums)
        print(nums)
