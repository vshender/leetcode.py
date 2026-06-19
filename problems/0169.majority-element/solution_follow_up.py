"""169. Majority Element

Uses Boyer-Moore voting: keeps one candidate and a counter that rises on a
matching value and falls on a different one, picking a new candidate whenever the
counter reaches zero.  The value appearing more than n/2 times outlasts every
cancellation, so it remains the candidate.  This takes O(n) time and O(1) space.
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """Return the majority element of `nums` (the value appearing more than n/2 times)."""

        candidate = 0
        count = 0

        # `count` is how far `candidate` leads the rest in the prefix seen so far.
        # At zero no value leads, so the next value becomes the new candidate.
        for num in nums:
            if count == 0:
                candidate = num

            count += 1 if num == candidate else -1

        return candidate


if __name__ == "__main__":
    sol = Solution()
    for nums in [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2],
    ]:
        print(f"{nums} -> {sol.majorityElement(nums)}")
