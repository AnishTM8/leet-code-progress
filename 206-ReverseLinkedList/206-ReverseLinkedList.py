# Last updated: 7/2/2025, 4:49:17 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev