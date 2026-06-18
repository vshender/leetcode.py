"""680. Valid Palindrome II

Walks two pointers inward.  On the first mismatch it spends the single allowed
deletion on either the left or the right character and rechecks the rest; `s`
works if either choice does.  A `deleted` flag lets one recursive helper do both
jobs: the lenient first pass and the strict check after a deletion is used.
This takes O(n) time and O(1) space.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        """Check whether `s` can become a palindrome after deleting at most one character."""

        return self.is_palindrome(s, 0, len(s) - 1)

    def is_palindrome(self, s: str, left: int, right: int, deleted: bool = False) -> bool:
        """Check whether `s[left..right]` is a palindrome, allowing one deletion unless `deleted`."""

        while left < right:
            if s[left] != s[right]:
                if deleted:
                    return False
                # Use the one deletion on `s[left]` or on `s[right]`.
                return (
                    self.is_palindrome(s, left + 1, right, True)
                    or self.is_palindrome(s, left, right - 1, True)
                )

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    sol = Solution()
    for s in [
        "aba",
        "abca",
        "abc",
        "ababb",
        "a",
        "ab",
        "",
        "acxcybycxcxa",
        "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga",
    ]:
        print(f"{s!r} -> {sol.validPalindrome(s)}")
