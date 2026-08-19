class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_stack.append(val)
            
        if self.stack:
            if val <= self.min_stack[0]:
                self.min_stack.insert(0, val)
        self.stack.append(val)
    def pop(self) -> None:
        
        if self.stack[-1] == self.min_stack[0]:
            self.min_stack.pop(0)
        self.stack = self.stack[:-1]

       
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[0]