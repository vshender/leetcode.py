"""206. Reverse Linked List

Scans the list once, prepending a copy of each value to a new list, so the values
come out in reverse order.  This takes O(n) time and O(n) space.
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

        reversed_head = None
        while head is not None:
            # Put a copy of the current head in front of the reversed part.
            reversed_head = ListNode(head.val, reversed_head)
            head = head.next

        return reversed_head


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
