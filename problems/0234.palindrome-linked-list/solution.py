"""234. Palindrome Linked List

Recurses to the tail, then compares the list from both ends while the call stack
unwinds: a shared `front` pointer steps forward from the head, and each returning
frame hands back the matching node from the back.  This takes O(n) time and O(n)
space for the recursion stack.
"""

from __future__ import annotations

from typing import final


@final
class ListNode:
    """A singly linked list node."""

    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    # `front` walks forward from the head while the recursion walks back from the tail.
    front: ListNode | None = None

    def isPalindrome(self, head: ListNode | None) -> bool:
        """Return True if the list reads the same forwards and backwards."""

        self.front = head
        return self.check_outward(head)

    def check_outward(self, node: ListNode | None) -> bool:
        """Recurse to the tail, then match each node with `front` while unwinding."""

        if node is None:
            return True

        if not self.check_outward(node.next):
            return False

        # Here `node` is the mirror of `front`, so both are non-None.
        assert self.front is not None
        if node.val != self.front.val:
            return False

        self.front = self.front.next
        return True


def linked_list_from_list(items: list[int]) -> ListNode | None:
    """Return a linked list containing the items of the given list."""

    node: ListNode | None = None
    for item in reversed(items):
        node = ListNode(item, node)

    return node


def linked_list_to_list(node: ListNode | None) -> list[int]:
    """Return the linked-list values as a Python list."""

    items: list[int] = []
    while node is not None:
        items.append(node.val)
        node = node.next

    return items


if __name__ == "__main__":
    sol = Solution()
    for values in [
        [1, 2, 2, 1],
        [1, 2],
        [1],
        [],
    ]:
        head = linked_list_from_list(values)
        print(f"{values} -> {sol.isPalindrome(head)}")
