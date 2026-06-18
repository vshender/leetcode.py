"""4. Median of Two Sorted Arrays

Merges the two sorted arrays with two pointers, but walks only as far as the
middle.  Keeps the last two merged values, which are the one or two elements the
median is built from.  This takes O(m + n) time and O(1) space.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """Return the median of the two sorted arrays."""

        len1, len2 = len(nums1), len(nums2)
        total = len1 + len2
        if total == 0:
            return 0.0

        i = j = 0
        prev = cur = 0.0
        # Pull the smaller head each step until `cur` reaches the middle element.
        # `prev` keeps the value from the step before, so `prev` and `cur` are the
        # middle pair when `total` is even.
        for _ in range(total // 2 + 1):
            prev = cur
            head1 = nums1[i] if i < len1 else float("inf")
            head2 = nums2[j] if j < len2 else float("inf")
            if head1 < head2:
                cur = head1
                i += 1
            else:
                cur = head2
                j += 1

        if total % 2 == 1:
            return cur
        else:
            return (prev + cur) / 2


if __name__ == "__main__":
    sol = Solution()
    for nums1, nums2 in [
        ([], []),
        ([1], []),
        ([], [1]),
        ([1], [2]),
        ([1, 3], [2]),
        ([1, 2], [3, 4]),
    ]:
        print(f"{nums1}, {nums2} -> {sol.findMedianSortedArrays(nums1, nums2)}")
