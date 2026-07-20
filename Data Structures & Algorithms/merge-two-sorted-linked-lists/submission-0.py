# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = ListNode()
        d = x

        while l1 and l2:
            if l1.val < l2.val:
                d.next = l1
                l1 = l1.next
            else:
                d.next = l2
                l2 = l2.next
            d = d.next
        
        if l1:
            d.next = l1
        elif l2:
            d.next = l2
        
        return x.next

