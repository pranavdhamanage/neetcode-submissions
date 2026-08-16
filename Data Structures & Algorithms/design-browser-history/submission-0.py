class ListNode:
    def __init__(self, val=None, prev = None, next=None):
        self.prev = prev
        self.next = next
        self.val = val
        

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode()
        self.tail = ListNode()
        node = ListNode(homepage)
        self.head.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = self.head
        self.curr = node
        
    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.curr.next = node
        node.next = self.tail
        node.prev = self.curr
        self.tail.prev = node
        self.curr = node

    def back(self, steps: int) -> str:
        while self.curr.prev != self.head and steps > 0:
            self.curr = self.curr.prev
            steps -= 1

        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next != self.tail and steps > 0:
            self.curr = self.curr.next
            steps -= 1

        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)