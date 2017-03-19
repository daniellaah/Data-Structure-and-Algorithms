"""155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_stack = []
        self.sub_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.main_stack.append(x)
        if not self.sub_stack or x < self.sub_stack[-1]:
            self.sub_stack.append(x)
        else:
            self.sub_stack.append(self.sub_stack[-1])


    def pop(self):
        """
        :rtype: void
        """
        self.sub_stack.pop()
        self.main_stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.main_stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.sub_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
