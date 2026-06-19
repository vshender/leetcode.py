"""1876. Substrings of Size Three with Distinct Characters

Slides a fixed window of size 3 over `s`, keeping a per-letter count for the
window and how many distinct letters it holds.  A window is good when all three
letters are distinct.  This takes O(n) time and O(1) space.
"""

from collections import defaultdict


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        """Count the length-3 substrings of `s` whose characters are all distinct."""

        good_count = 0
        window_counts: defaultdict[str, int] = defaultdict(int)
        distinct_letters = 0

        for i, char in enumerate(s):
            # Add the entering character.
            if window_counts[char] == 0:
                distinct_letters += 1
            window_counts[char] += 1

            # Drop the character that just left the size-3 window.
            if i >= 3:
                left = s[i - 3]
                window_counts[left] -= 1
                if window_counts[left] == 0:
                    distinct_letters -= 1

            if distinct_letters == 3:
                good_count += 1

        return good_count


if __name__ == "__main__":
    sol = Solution()
    for s in [
        "xyzzaz",
        "aababcabc",
    ]:
        print(f"{s} -> {sol.countGoodSubstrings(s)}")
