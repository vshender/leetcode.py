"""234. Palindrome Linked List

Finds the middle with a slow and a fast pointer, reverses the second half in place,
walks the two halves inward comparing values, then reverses the second half back to
restore the original list.  This takes O(n) time and O(1) space.
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
    def isPalindrome(self, head: ListNode | None) -> bool:
        """Return True if the list reads the same forwards and backwards."""

        # Reverse the second half so it can be read back to front.
        second_half = self.reverse(self.find_middle(head))

        # Walk the first half and the reversed second half together.
        is_palindrome = True
        first, second = head, second_half
        while is_palindrome and second is not None:
            assert first is not None
            if first.val != second.val:
                is_palindrome = False
            first = first.next
            second = second.next

        # Restore the list by reversing the second half back.
        _ = self.reverse(second_half)
        return is_palindrome

    def find_middle(self, head: ListNode | None) -> ListNode | None:
        """Return the start of the second half (the middle node when length is odd)."""

        # `fast` moves twice as fast, so `slow` reaches the middle when `fast` ends.
        slow = fast = head
        while fast is not None and fast.next is not None:
            assert slow is not None
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, head: ListNode | None) -> ListNode | None:
        """Reverse the list in place and return the new head."""

        prev = None
        while head is not None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        return prev


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
