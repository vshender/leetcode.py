"""206. Reverse Linked List

Reverses the list with tail recursion: each call peels the head and prepends it to
an accumulator that holds the already-reversed part, which becomes the answer once
the input runs out.  This takes O(n) time and O(n) space.
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
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """Reverse the linked list and return the new head."""

        return self.reverse_onto(head, None)

    def reverse_onto(self, head: ListNode | None, reversed_head: ListNode | None) -> ListNode | None:
        """Prepend each value of `head` onto `reversed_head` and return the result."""

        if head is None:
            return reversed_head

        # Copy the current head in front of the reversed part, then recurse on the rest.
        return self.reverse_onto(head.next, ListNode(head.val, reversed_head))


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
        [1, 2, 3, 4, 5],
        [1, 2],
        [1],
        [],
    ]:
        head = linked_list_from_list(values)
        reversed_node = sol.reverseList(head)
        reversed_list = linked_list_to_list(reversed_node)
        print(f"{values} -> {reversed_list}")
