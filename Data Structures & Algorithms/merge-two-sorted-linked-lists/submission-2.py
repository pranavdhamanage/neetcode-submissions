# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        n = d = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                n.next = l1
                l1 = l1.next
            else:
                n.next = l2
                l2 = l2.next
            
            n = n.next
        
        n.next = l1 or l2

        return d.next