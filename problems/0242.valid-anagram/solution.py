"""242. Valid Anagram

Counts the characters of each string and compares the two counts: equal counts
mean one string is a rearrangement of the other.  This takes O(n) time and
O(min(n, alphabet)) space.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Check whether `t` is an anagram of `s`."""

        return Counter(s) == Counter(t)


if __name__ == "__main__":
    sol = Solution()
    for s, t in [
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("", ""),
    ]:
        print(f"s = {s!r}, t = {t!r} -> {sol.isAnagram(s, t)}")
