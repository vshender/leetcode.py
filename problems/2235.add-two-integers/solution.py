# 2235. Add Two Integers

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        """Return the sum of two integers."""

        return num1 + num2

if __name__ == "__main__":
    sol = Solution()
    x = 27
    y = 42
    print(f"{x} + {y} =", sol.sum(27, 42))
