"""290. Word Pattern

Maps each pattern letter to a word with a hash map, failing as soon as a letter
is seen mapping to two different words.  A length check and a final one-to-one
check keep the match a true bijection: distinct letters must map to distinct
words.  This takes O(n) time and O(n) space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """Check whether `s` follows `pattern`."""

        words = s.split()
        if len(pattern) != len(words):
            return False

        word_mapping: dict[str, str] = {}
        for char, word in zip(pattern, words):
            if word_mapping.setdefault(char, word) != word:
                return False

        # The match must be one-to-one: two letters mapping to the same word
        # would break the pattern, so distinct keys need distinct values.
        return len(word_mapping) == len(set(word_mapping.values()))


if __name__ == "__main__":
    sol = Solution()
    for pattern, s in [
        ("abba", "dog cat cat dog"),
        ("abba", "dog cat cat fish"),
        ("aaaa", "dog cat cat dog"),
        ("aaab", "dog dog dog dog"),
        ("", ""),
    ]:
        print(f"pattern = {pattern!r}, s = {s!r} -> {sol.wordPattern(pattern, s)}")
