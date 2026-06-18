"""3. Longest Substring Without Repeating Characters

Uses the sliding window technique with a set of the characters in the window.
When a character repeats, the left edge moves right one step at a time and drops
characters until the repeat is gone.  The inner loop looks like extra work, but
each character is added once and removed once, so the total work stays O(n).
This takes O(n) time and O(min(n, alphabet)) space.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Find the length of the longest substring without repeating
        characters.
        """

        window_chars: set[str] = set()
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char not in window_chars:
                window_chars.add(char)

            else:
                # `char` is already in the window.  Remove every character
                # before the earlier copy of `char`, then move `left` past
                # that copy.  `char` stays in the set as the new copy.
                while s[left] != char:
                    window_chars.remove(s[left])
                    left += 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    sol = Solution()
    for s in [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "tmmzuxt",
    ]:
        print(f"{s}: {sol.lengthOfLongestSubstring(s)}")
