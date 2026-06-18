"""125. Valid Palindrome

Uses the two-pointer technique.  Two pointers start at both ends and move
inward, each skipping any non-alphanumeric character, and compare the remaining
characters case-insensitively.  The string is a palindrome when the pointers
meet without a mismatch.  This takes O(n) time and O(1) space.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Check whether the string is a palindrome, ignoring case and non-alphanumeric characters."""

        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True


if __name__ == "__main__":
    sol = Solution()
    for s in [
        "amanaplanacanalpanama",
        "race a car",
        " ",
        "",
    ]:
        print(f"{s!r} -> {sol.isPalindrome(s)}")
