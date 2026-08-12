class MinStack:

    def __init__(self):
        self.min_idx_stack = []
        self.el_stack = []
        self.curr_min = float('inf')
        self.el_idx = -1

    def push(self, val: int) -> None:
        self.el_stack.append(val)
        self.el_idx += 1
        if val <= self.getMin():
            self.curr_min = val
            self.min_idx_stack.append(self.el_idx)


    def pop(self) -> None:
        if self.top() == self.curr_min:    
            self.min_idx_stack.pop()
            if self.min_idx_stack:
                self.curr_min = self.el_stack[self.min_idx_stack[-1]]
            else:
                self.curr_min = float('inf')
        self.el_stack.pop()

        self.el_idx -= 1

    def top(self) -> int:
        return self.el_stack[self.el_idx]

    def getMin(self) -> int:
        return self.curr_min
