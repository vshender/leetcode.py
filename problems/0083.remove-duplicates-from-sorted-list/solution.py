"""83. Remove Duplicates from Sorted List

Walks the sorted list once with a single pointer; because equal values sit next
to each other, it unlinks any node whose value matches the next node's.  This
takes O(n) time and O(1) space.
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
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        """Delete duplicates from the sorted list."""

        pointer = head
        while pointer is not None:
            # Duplicates are adjacent in a sorted list, so compare neighbors.
            if pointer.next is not None and pointer.val == pointer.next.val:
                # Unlink the duplicate but stay on `pointer` to skip a run of equals.
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next

        return head


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
        [1, 1, 2],
        [1, 1, 2, 3, 3],
        [],
        [1, 1, 1],
    ]:
        head = linked_list_from_list(values)
        deduped = sol.deleteDuplicates(head)
        result = linked_list_to_list(deduped)
        print(f"{values} -> {result}")
