"""392. Is Subsequence: Follow-Up

Preprocesses `t` once into the sorted positions of each letter, then answers
each query with binary search: for every character of `s` it finds the nearest
position in `t` strictly after the previous match, so a query fails as soon as
a character has no such position.  Preprocessing takes O(|t|) time and space,
and each query then takes O(|s| * log |t|) time.
"""

from bisect import bisect_right
from collections import defaultdict


class Solution:
    def isSubsequence(self, ss: list[str], t: str) -> list[bool]:
        """Check whether the strings from `ss` are subsequences of `t`."""

        letter_positions: defaultdict[str, list[int]] = defaultdict(list)
        for pos, char in enumerate(t):
            letter_positions[char].append(pos)

        results: list[bool] = []
        for s in ss:
            last_pos = -1  # last position matched in `t`, shared across all of `s`
            for char in s:
                positions = letter_positions.get(char, ())
                # Index of the first position of `char` strictly after `last_pos`.
                next_idx = bisect_right(positions, last_pos)
                if next_idx >= len(positions):
                    results.append(False)
                    break
                last_pos = positions[next_idx]
            else:
                results.append(True)

        return results


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("ahbgdc", ["abc", "axc", "", "ba", "aa", "ahbgdc", "ahgdc", "z"]),
        ("ab", ["ab", "ba", "a", "b", "aa", ""]),
        ("bbbbba", ["a", "aa", "ba", "ab"]),
        ("baa", ["aa", "aaa", "ba", "ab"]),
        ("aXaXa", ["aaa", "aaaa"]),
        ("", ["", "a"]),
    ]
    for t, ss in test_cases:
        results = sol.isSubsequence(ss, t)
        for s, is_subsequence in zip(ss, results):
            print(f"s = {s!r}, t = {t!r} -> {is_subsequence}")
        print()
