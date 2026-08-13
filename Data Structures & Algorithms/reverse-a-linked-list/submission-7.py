# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head

        if not h:
            return None

        nh = h
        if h.next:
            nh = self.reverseList(h.next)
            h.next.next = h

        h.next = None
        return nh