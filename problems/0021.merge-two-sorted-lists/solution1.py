"""21. Merge Two Sorted Lists

Merges the lists recursively: when both are non-empty, takes the smaller head and
links it to the merge of the rest; an empty list ends the recursion.  This takes
O(n + m) time and O(n + m) space.
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

        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        else:
            return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))


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
