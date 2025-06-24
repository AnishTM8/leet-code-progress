# Last updated: 6/23/2025, 11:24:32 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return

        prev = None

        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

            