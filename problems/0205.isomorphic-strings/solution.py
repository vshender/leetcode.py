"""205. Isomorphic Strings

Maps each character of `s` to a character of `t` with a hash map, failing as soon
as some character is seen mapping to two different targets.  A final check keeps
the mapping one-to-one: distinct source characters must map to distinct targets.
This takes O(n) time and O(min(n, alphabet)) space.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """Check whether `s` and `t` are isomorphic."""

        letter_mapping: dict[str, str] = {}
        for s_char, t_char in zip(s, t):
            if letter_mapping.setdefault(s_char, t_char) != t_char:
                return False

        # The mapping must be one-to-one: two source characters mapping to the
        # same target would break isomorphism, so distinct keys need distinct
        # values.
        return len(letter_mapping) == len(set(letter_mapping.values()))


if __name__ == "__main__":
    sol = Solution()
    for s, t in [
        ("egg", "add"),
        ("f11", "b23"),
        ("paper", "title"),
        ("aa", "ab"),
        ("ab", "aa"),
        ("", ""),
    ]:
        print(f"s = {s!r}, t = {t!r} -> {sol.isIsomorphic(s, t)}")
