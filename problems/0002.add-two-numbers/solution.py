"""2. Add Two Numbers

Adds matching digits from both reversed linked lists, carrying any overflow to
the next node.  This takes O(max(m, n)) time and O(max(m, n)) space for the new
list and the recursion stack.
"""

from __future__ import annotations

from typing import final


# Definition for singly-linked list.
@final
class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: ListNode | None,
        l2: ListNode | None,
        carry: int = 0,
    ) -> ListNode | None:
        """Return the digit-wise sum of two reversed digit lists as a new list."""

        if l1 is None and l2 is None and carry == 0:
            return None

        digit1, next1 = (l1.val, l1.next) if l1 is not None else (0, None)
        digit2, next2 = (l2.val, l2.next) if l2 is not None else (0, None)
        total = digit1 + digit2 + carry
        return ListNode(
            val=total % 10,
            next=self.addTwoNumbers(next1, next2, carry=total // 10),
        )


def list_node_from_list(digits: list[int]) -> ListNode | None:
    """Return a linked list containing the given digits in order."""

    node: ListNode | None = None
    for digit in reversed(digits):
        node = ListNode(digit, node)

    return node


def list_node_to_list(node: ListNode | None) -> list[int]:
    """Return the linked-list values as a Python list."""

    digits: list[int] = []
    while node is not None:
        digits.append(node.val)
        node = node.next

    return digits


if __name__ == "__main__":
    sol = Solution()
    l1 = list_node_from_list([9, 9, 9, 9, 9, 9, 9])
    l2 = list_node_from_list([9, 9, 9, 9])
    sum = sol.addTwoNumbers(l1, l2)
    print(list_node_to_list(sum))
