# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(-1)
        current = dummy

        carry = 0

        while l1 or l2:
            sum = carry
            if l1:
                sum = sum + l1.val
            if l2:
                sum = sum + l2.val

            new_node = ListNode(sum % 10)
            carry = sum / 10
            current.next = new_node
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            new_node = ListNode(carry)
            current.next = new_node
            

        return dummy.next



# Logic for revision:

# Use a dummy node to build the result list without special head handling.
# Traverse while at least one list still has nodes (lists may be unequal length).
# At each step, add digits from l1 and l2 along with carry from previous sum.
# Create a new node with digit = sum % 10 and update carry using sum // 10.
# Move pointers forward in both lists when available.
# After traversal, append a final node if a carry remains.

        