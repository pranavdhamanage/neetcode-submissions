class ListNode:
    def __init__(self,val,prev = None,next = None):
        self.prev = prev
        self.next = next
        self.val = val

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr!=self.tail and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        n = ListNode(val)
        n.prev = self.head
        n.next = self.head.next
        self.head.next.prev = n
        self.head.next = n
        

    def addAtTail(self, val: int) -> None:
        n = ListNode(val)
        n.next = self.tail
        n.prev = self.tail.prev
        self.tail.prev.next = n
        self.tail.prev = n

    def addAtIndex(self, index: int, val: int) -> None:
        n = ListNode(val)
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            n.prev = curr.prev
            n.next = curr
            curr.prev.next = n
            curr.prev = n


    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index == 0:
            next = curr.next
            prev = curr.prev
            next.prev = prev
            prev.next = next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)