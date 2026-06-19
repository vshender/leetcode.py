"""771. Jewels and Stones

Puts the jewel characters in a set, then counts the stones whose character is in
that set.  This takes O(j + s) time and O(j) space, for `j` jewels and `s` stones.
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """Return the number of stones that are also jewels."""

        jewel_set = set(jewels)
        return sum(stone in jewel_set for stone in stones)


if __name__ == "__main__":
    sol = Solution()
    for jewels, stones in [
        ("aA", "aAAbbbb"),
        ("z", "ZZ"),
        ("", "abc"),
        ("aA", ""),
        ("", ""),
    ]:
        print(f"jewels = {jewels!r}, stones = {stones!r} -> {sol.numJewelsInStones(jewels, stones)}")
