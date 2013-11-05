
class StackQueue(object):

    def __init__(self, *args):
        self.stack1 = []
        self.stack2 = []
        self.enqueue(*args)

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def isEmpty(self):
        return not self.size()

    def __swap(self):
        if self.stack1:
            raise AttributeError('Not allowed to copy on non-empty stack')
        self.stack1 = self.stack2[::-1]
        self.stack2 = []

    def dequeue(self):
        """Get from queue and remove"""
        if self.isEmpty():
            raise ValueError('dequeue on empty queue')
        if not self.stack1:
            self.__swap()
        return self.stack1.pop()

    def get(self):
        """Get from queue"""
        if self.isEmpty():
            raise ValueError('get on empty queue')
        if self.stack1:
            return self.stack1[-1]
        return self.stack2[0]

    def enqueue(self, *args):
        """Add elements into queue"""
        if self.isEmpty():
            self.stack1.extend(args[::-1])
        else:
            self.stack2.extend(args)

    def __iter__(self):
        return self

    def next(self):
        while not self.isEmpty():
            return self.dequeue()
        raise StopIteration
