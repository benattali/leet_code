class MyQueue:

    def __init__(self):
        self.queue = []
        return

    def push(self, x: int) -> None:
        self.queue.append(x)
        return

    def pop(self) -> int:
        if not self.queue:
            return

        popped_item = self.queue[0]
        del self.queue[0]
        return popped_item

    def peek(self) -> int:
        return self.queue[0] if self.queue else None

    def empty(self) -> bool:
        return True if not self.queue else False

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print("\nobj", obj.queue)
print("peek", obj.peek())
print("pop", obj.pop())
print("empty?", obj.empty())
