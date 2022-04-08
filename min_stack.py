class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1] if self.stack else []

    def getMin(self) -> int:
        if self.stack:
            minElement = min(self.stack)
            return minElement



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_4 = obj.getMin()
print(param_4)
# print(obj.__dict__)
obj.pop()
# print(obj.__dict__)
param_3 = obj.top()
print(param_3)
# print(obj.__dict__)
param_4 = obj.getMin()
print(param_4)
# print(obj.__dict__)
