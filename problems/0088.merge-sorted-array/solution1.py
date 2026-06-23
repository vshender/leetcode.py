"""88. Merge Sorted Array

Merges the two sorted arrays front to back into a scratch array with the classic
two-pointer merge, then copies the result back into `nums1`.  This takes O(m + n)
time and O(m + n) space.
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """Merge `nums2` into `nums1` in place so `nums1` stays sorted."""

        merged = [0] * len(nums1)

        i, j = 0, 0
        while i < m or j < n:
            # `i + j` is how many values are already placed, so it is the next
            # write position in `merged`.
            if i < m and (j == n or nums1[i] <= nums2[j]):
                merged[i + j] = nums1[i]
                i += 1
            else:
                merged[i + j] = nums2[j]
                j += 1

        nums1[:] = merged


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
