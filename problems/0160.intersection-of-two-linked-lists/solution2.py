"""160. Intersection of Two Linked Lists

Walks two pointers, one from each head; when a pointer reaches the end it jumps to
the other list's head.  After the switch both pointers have walked m + n nodes, so
they are aligned and meet at the shared node, or land on None together when the
lists do not intersect.  This takes O(m + n) time and O(1) space.
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

        nodeA: ListNode | None = headA
        nodeB: ListNode | None = headB

        # Each pointer crosses into the other list once it ends, so both cover
        # m + n nodes and become aligned.  When they point at the same node it is
        # the intersection; with no intersection both reach None on the same step.
        while nodeA is not nodeB:
            nodeA = nodeA.next if nodeA is not None else headB
            nodeB = nodeB.next if nodeB is not None else headA

        return nodeA


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
