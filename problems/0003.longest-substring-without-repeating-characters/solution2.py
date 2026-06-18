"""3. Longest Substring Without Repeating Characters

Uses the sliding window technique with a dictionary that maps each character to
its last seen index.  When a character repeats, the left edge jumps straight to
the position after the previous copy.  This takes O(n) time and
O(min(n, alphabet)) space.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Find the length of the longest substring without repeating
        characters.
        """

        char_index: dict[str, int] = {}  # char -> last seen index
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            # Move `left` only if the previous occurrence of `char` is inside
            # the window; its index may already be outside it.
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
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
