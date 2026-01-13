# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy
        
        for i in range(n):
            fast = fast.next

        if not fast:
            dummy.next = dummy.next.next
            return dummy.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next


# Logic:
# Use a dummy node to handle edge cases where the head is removed.
# Move the fast pointer exactly n steps ahead to create a fixed gap.
# Move both fast and slow pointers together until fast reaches the last node.
# At this point, slow is just before the node to delete.
# Remove the node by skipping it (slow.next = slow.next.next).
# Return dummy.next as the new head.
