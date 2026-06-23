"""88. Merge Sorted Array

Merges the two sorted arrays from the back into the free tail of `nums1`, each
step writing the larger remaining value.  Writing back to front never overwrites
a `nums1` value that has not been read yet, so no extra array is needed.  This
takes O(m + n) time and O(1) space.
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """Merge nums2 into nums1 in place so nums1 stays sorted."""

        i = m - 1
        j = n - 1
        write_idx = len(nums1) - 1

        # Once `nums2` is used up, the remaining `nums1` values are already in
        # their final places, so stop.
        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[write_idx] = nums1[i]
                i -= 1
            else:
                nums1[write_idx] = nums2[j]
                j -= 1

            write_idx -= 1


if __name__ == "__main__":
    sol = Solution()
    for nums1, m, nums2, n in [
        ([1,2,3,0,0,0], 3, [2,5,6], 3),
        ([1], 1, [], 0),
        ([0], 0, [1], 1),
        ([], 0, [], 0),
    ]:
        print(f"nums1 = {nums1[:m]}, nums2 = {nums2} -> ", end="")
        sol.merge(nums1, m, nums2, n)
        print(nums1)
