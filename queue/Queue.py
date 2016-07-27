# Queue class for generic queueing


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.isEmpty():
            return 'Nothing to dequeue.'
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def __str__(self):
        return ', '.join(self.items)
