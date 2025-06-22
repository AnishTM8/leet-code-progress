# Last updated: 6/22/2025, 7:15:43 PM
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
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        max_sum = 0

        while slow:
            max_sum = max(max_sum, slow.val + prev.val)
            prev = prev.next
            slow = slow.next
        return max_sum
