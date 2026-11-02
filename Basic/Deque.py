from collections import deque

class MyDeque:
    def __init__(self):
        self.d = deque()

    def addFront(self, x):
        self.d.appendleft(x)

    def addBack(self, x):
        self.d.append(x)

    def removeFront(self):
        return self.d.popleft() if self.d else -1

    def removeBack(self):
        return self.d.pop() if self.d else -1

    def elementAtFront(self):
        return self.d[0] if self.d else -1

    def elementAtBack(self):
        return self.d[-1] if self.d else -1

    def isEmpty(self):
        return len(self.d) == 0

    def size(self):
        return len(self.d)
