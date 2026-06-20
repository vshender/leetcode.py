"""21. Merge Two Sorted Lists

Walks both lists with a dummy head, repeatedly appending a copy of the smaller
current value and advancing that list, until both are exhausted.  This takes
O(n + m) time and O(1) extra space.
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
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        """Merge two sorted lists into one sorted list."""

        pointer = dummy = ListNode(0, None)

        while list1 is not None or list2 is not None:
            if list1 is None or (list2 is not None and list2.val < list1.val):
                assert list2 is not None
                val, list2 = list2.val, list2.next
            else:
                val, list1 = list1.val, list1.next

            pointer.next = ListNode(val, None)
            pointer = pointer.next

        return dummy.next


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
    for list1, list2 in [
        ([1, 2, 4], [1, 3, 4]),
        ([], []),
        ([], [0]),
    ]:
        ll1 = linked_list_from_list(list1)
        ll2 = linked_list_from_list(list2)
        llm = sol.mergeTwoLists(ll1, ll2)
        listm = linked_list_to_list(llm)
        print(f"merge({list1}, {list2}) = {listm}")
