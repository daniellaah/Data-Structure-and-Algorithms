"""225. Implement Stack using Queues
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack)."""
class MyQueue(object):
    def __init__(self):
        self.array = []

    def put(self, x):
        self.array.insert(0, x)

    def get(self):
        return self.array.pop()

    def isEmpty(self):
        return True if len(self.array) == 0 else False

    def size(self):
        return len(array)

# 使用两个队列
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = MyQueue()
        self.queue2 = MyQueue()


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if not self.queue1.isEmpty():
            self.queue1.put(x)
        else:
            self.queue2.put(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if not self.queue1.isEmpty():
            while True:
                x = self.queue1.get()
                if not self.queue1.isEmpty():
                    self.queue2.put(x)
                else:
                    return x
        elif not self.queue2.isEmpty():
            while True:
                x = self.queue2.get()
                if not self.queue2.isEmpty():
                    self.queue1.put(x)
                else:
                    return x
        else:
            return None


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if not self.queue1.isEmpty():
            while True:
                x = self.queue1.get()
                self.queue2.put(x)
                if self.queue1.isEmpty():
                    return x
        elif not self.queue2.isEmpty():
            while True:
                x = self.queue2.get()
                self.queue1.put(x)
                if self.queue2.isEmpty():
                    return x
        else:
            return None

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return True if self.queue1.isEmpty() and self.queue2.isEmpty() else False



class MyQueue(object):
    def __init__(self):
        self.array = []

    def push(self, x):
        self.array.insert(0, x)

    def pop(self):
        return self.array.pop()

    def peek(self):
        return self.array[-1]

    def isEmpty(self):
        return True if len(self.array) == 0 else False

    def size(self):
        return len(self.array)

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = MyQueue()


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.push(x)
        for i in range(self.queue.size()-1):
            self.queue.push(self.queue.peek())
            self.queue.pop()


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue.pop()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue.peek()


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue.isEmpty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
