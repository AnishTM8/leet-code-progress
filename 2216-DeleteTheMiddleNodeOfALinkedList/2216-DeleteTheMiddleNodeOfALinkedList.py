# Last updated: 6/22/2025, 7:15:41 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next == None:
            return None
        slow = fast = head
        prev = None

        while fast != None and fast.next != None:
            prev = slow
            fast = fast.next.next
            slow = slow.next

        prev.next = prev.next.next
        return head