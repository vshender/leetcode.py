"""392. Is Subsequence

Uses the two-pointer technique.  One pointer walks `t` once while another tracks
how much of `s` has been matched; whenever the next needed character of `s`
appears in `t`, the match advances.  `s` is a subsequence when every character
is matched.  This takes O(n) time and O(1) space, where n is the length of `t`.
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """Check whether `s` is a subsequence of `t`."""

        # Walk `t` once, advancing through `s` each time the next needed
        # character shows up.  The `s_idx < len(s)` guard also covers the empty
        # `s` case, where nothing needs matching.
        s_idx = 0
        for char in t:
            if s_idx < len(s) and s[s_idx] == char:
                s_idx += 1

        return s_idx == len(s)


if __name__ == "__main__":
    sol = Solution()
    for s, t in [
        ("abc", "ahbgdc"),
        ("axc", "ahbgdc"),
        ("", "abc"),
        ("abc", ""),
        ("", ""),
    ]:
        print(f"s = {s!r}, t = {t!r} -> {sol.isSubsequence(s, t)}")
