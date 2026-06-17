"""1. Two Sum

The two-pointers method runs on sorted value-index pairs.  Sorting keeps the
values ordered while preserving their original indices, then the pointers move
inward until they find the pair that adds up to the target.  This takes
O(n log n) time and O(n) space.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Return the indices of two numbers that add up to the target."""

        # Create a list of `(value, original_index)` tuples to preserve indices
        # after sorting.
        indexed_nums = list(zip(nums, range(len(nums))))

        indexed_nums.sort()

        # Two-pointer approach: start from both ends of the sorted list.
        i, j = 0, len(nums) - 1
        while i < j:
            left_val, left_idx = indexed_nums[i]
            right_val, right_idx = indexed_nums[j]
            cur_sum = left_val + right_val
            if cur_sum < target:
                i += 1
            elif cur_sum > target:
                j -= 1
            else:
                # Found the pair, return their original indices.
                return [left_idx, right_idx]

        return []


if __name__ == "__main__":
    nums = [11, 2, 15, 7]
    target = 9

    s = Solution()
    print(s.twoSum(nums, target))
