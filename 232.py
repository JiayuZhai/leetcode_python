class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stact = []
        self.queue = []
        self.len = 0

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stact.append(x)
        self.len +=1
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while len(self.stact)!=0:
            self.queue.append(self.stact.pop())
        x = self.queue.pop()
        while len(self.queue)!=0:
            self.stact.append(self.queue.pop())
        self.len-=1
        return x

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while len(self.stact)!=0:
            self.queue.append(self.stact.pop())

        x = self.queue.pop()
        self.queue.append(x)

        while len(self.queue)!= 0:
            self.stact.append(self.queue.pop())
        return x

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.len:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
