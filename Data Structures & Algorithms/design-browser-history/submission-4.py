class BrowserHistory:

    def __init__(self, homepage: str):
        self.f_stack = []
        self.b_stack = [homepage]
        self.curr = homepage

    def visit(self, url: str) -> None:
        self.f_stack = []
        self.b_stack.append(url)
        self.curr = url

    def back(self, steps: int) -> str:
        while len(self.b_stack) and steps > 0:
            val = self.b_stack.pop()
            self.f_stack.append(val)
            steps -= 1

        if len(self.b_stack):
            self.curr = self.b_stack[-1]
        else:
            self.curr = self.f_stack[-1]

        return self.curr

    def forward(self, steps: int) -> str:
        while len(self.f_stack) and steps > 0:
            val = self.f_stack.pop()
            self.b_stack.append(val)
            steps -= 1
        
        if len(self.b_stack):
            self.curr = self.b_stack[-1]
        
        return self.curr



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)