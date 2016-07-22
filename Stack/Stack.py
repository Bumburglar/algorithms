class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return item

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return "Error: Stack is empty."

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.isEmpty():
            return self.items[self.size() - 1]
        else:
            return "N/A"
