# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow,fast = head,head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        # reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        
        maxSum = 0
        left = head
        right = prev

        while right:
            maxSum = max(maxSum, left.val + right.val)
            left = left.next
            right = right.next
        
        return maxSum



# Logic:
# Use fast and slow pointers to locate the start of the second half of the list.
# Reverse the second half of the linked list in-place to simulate backward traversal.
# Initialize two pointers: one at the head of the list and one at the reversed second half.
# Traverse both halves together, computing twin sums for corresponding nodes.
# Track and return the maximum twin sum encountered.


       



        