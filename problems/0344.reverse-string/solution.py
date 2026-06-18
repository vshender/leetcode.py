"""344. Reverse String

Uses the two-pointer technique in place.  Two pointers start at both ends and
swap the characters they point to, then step toward the middle until they meet.
This takes O(n) time and O(1) space.
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """Reverse the list of characters in place."""

        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    sol = Solution()
    for s in [
        ["h", "e", "l", "l", "o"],
        ["H", "a", "n", "n", "a", "h"],
    ]:
        print(f"{s} -> ", end="")
        sol.reverseString(s)
        print(s)
