"""160. Intersection of Two Linked Lists

Measures both lists, then advances the longer one by the length difference so the
two pointers are the same distance from the end, and walks them together until
they meet at the shared node (or both run off the end).  This takes O(m + n) time
and O(1) space.
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        """Return the node where the two lists intersect, or None."""

        len_a = self.get_linked_list_length(headA)
        len_b = self.get_linked_list_length(headB)

        # Drop the longer list's head start so both are the same distance from the end.
        nodeA = self.skip_nodes(headA, max(len_a - len_b, 0))
        nodeB = self.skip_nodes(headB, max(len_b - len_a, 0))

        # Now they step in lockstep, so they reach the shared node (or None) together.
        while nodeA is not nodeB:
            assert nodeA is not None and nodeB is not None
            nodeA = nodeA.next
            nodeB = nodeB.next

        return nodeA

    def get_linked_list_length(self, node: ListNode | None) -> int:
        """Return the number of nodes in the list."""

        length = 0
        while node is not None:
            length += 1
            node = node.next

        return length

    def skip_nodes(self, node: ListNode | None, n: int) -> ListNode | None:
        """Return the node `n` steps ahead, or None if the list ends first."""

        while node is not None and n > 0:
            n -= 1
            node = node.next

        return node


def linked_list_to_list(node: ListNode | None) -> list[int]:
    """Return the linked-list values as a Python list."""

    items: list[int] = []
    while node is not None:
        items.append(node.val)
        node = node.next

    return items


if __name__ == "__main__":
    common_tail = ListNode(8, ListNode(4, ListNode(5, None)))
    headA = ListNode(4, ListNode(1, common_tail))
    headB = ListNode(5, ListNode(6, ListNode(1, common_tail)))
    intersection = Solution().getIntersectionNode(headA, headB)
    print(linked_list_to_list(intersection))
