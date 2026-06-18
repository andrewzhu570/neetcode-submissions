class MinStack:

    def __init__(self):
        self.stk = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    def pop(self) -> None:
        self.stk.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
