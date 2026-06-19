"""383. Ransom Note

Counts the letters of each string; the note can be built when every letter is
needed no more often than the magazine provides it (the note's letter counts are
a sub-multiset of the magazine's).  This takes O(n) time and O(min(n, alphabet))
space.
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """Check whether `ransomNote` can be built from the letters of `magazine`."""

        return Counter(ransomNote) <= Counter(magazine)


if __name__ == "__main__":
    sol = Solution()
    for ransomNote, magazine in [
        ("a", "b"),
        ("aa", "ab"),
        ("aa", "aab"),
        ("", ""),
        ("abc", "abc"),
        ("aaabb", "aaaaabbbc"),
        ("aaabbd", "aaaaabbbc"),
    ]:
        print(f"ransomNote = {ransomNote!r}, magazine = {magazine!r} -> {sol.canConstruct(ransomNote, magazine)}")
