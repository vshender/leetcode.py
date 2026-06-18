"""680. Valid Palindrome II

Walks two pointers inward.  On the first mismatch it spends the single allowed
deletion on whichever side makes the characters line up and keeps going.  When
deleting either side would work the choice is ambiguous, so it records a
`savepoint`; if a later mismatch proves the first choice wrong, it jumps back to
the savepoint and tries the other side.  This takes O(n) time and O(1) space.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        """Check whether `s` can become a palindrome after deleting at most one character."""

        left, right = 0, len(s) - 1
        deleted = False        # whether the one allowed deletion is already used
        savepoint = None  # position to retry from when the delete choice was ambiguous

        while left < right:
            if s[left] != s[right]:
                if deleted:
                    if savepoint is not None:
                        # The delete-left guess failed; switch to the delete-right
                        # branch.  `savepoint` already holds the exact pair to
                        # examine, so `continue` to skip the end-of-loop step that
                        # would move both pointers past it.
                        left, right = savepoint
                        savepoint = None
                        continue
                    else:
                        return False

                elif s[left + 1] == s[right]:
                    # Delete `s[left]`.  If deleting `s[right]` would also match,
                    # the choice is ambiguous: save the pair to resume from in
                    # that case --- deleting `s[right]` keeps `left` and moves the
                    # right edge to `right - 1`.
                    if s[left] == s[right - 1]:
                        savepoint = (left, right - 1)

                    left += 1
                    deleted = True
                elif s[left] == s[right - 1]:
                    # Only deleting `s[right]` matches here.
                    right -= 1
                    deleted = True
                else:
                    return False

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
