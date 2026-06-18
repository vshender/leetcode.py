"""11. Container With Most Water

Uses the two-pointer technique.  Two pointers start at the outermost lines and
move inward.  The water is capped by the shorter of the two lines, so only
moving the shorter line inward can ever reach a taller line and a larger area —
moving the taller one keeps the same cap but shrinks the width.  Each line is
visited once.  This takes O(n) time and O(1) space.
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        """Find the largest area of water between two vertical lines."""

        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            cur_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, cur_area)

            # Move the shorter line inward; it is the one capping the area, so
            # it is the only side that has a chance to improve.  When the two
            # lines are equal, either side works.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    sol = Solution()
    for height in [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1],
        [1, 2, 1],
    ]:
        print(f"{height} -> {sol.maxArea(height)}")
