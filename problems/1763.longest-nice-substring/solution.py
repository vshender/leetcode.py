"""1763. Longest Nice Substring

Checks every substring by brute force.  A substring is nice when each letter in
it appears in both cases, tracked cheaply with a two-bit case mask per letter and
a counter of still-incomplete letters: the substring is nice exactly when that
counter is zero.  This takes O(n^2) time and O(n) space.
"""

from collections import defaultdict


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        """Return the longest nice substring, the earliest one if several tie."""

        best_start, best_len = 0, 0
        for i in range(len(s)):
            # `case_mask`: letter -> bits (0b01 lowercase seen, 0b10 uppercase).
            # `incomplete`: how many letters are present but still miss a case.
            case_mask: defaultdict[str, int] = defaultdict(int)
            incomplete = 0

            for j in range(i, len(s)):
                char = s[j]
                bit = 0b01 if char.islower() else 0b10
                letter = char.lower()

                before = case_mask[letter]
                case_mask[letter] = before | bit
                if before == 0:
                    incomplete += 1    # new letter, one case so far
                elif before != 0b11 and case_mask[letter] == 0b11:
                    incomplete -= 1    # this letter just got both cases

                # Record only the bounds; build the substring once at the end.
                if incomplete == 0 and j - i + 1 > best_len:
                    best_start, best_len = i, j - i + 1

        return s[best_start : best_start + best_len]


if __name__ == "__main__":
    sol = Solution()
    for s in [
        "YazaAay",
        "Bb",
        "c",
        "",
    ]:
        print(f"{s!r} -> {sol.longestNiceSubstring(s)!r}")
