# 225. Implement Stack using Queues
# ttungl@gmail.com
class MyStack(object):
	# runtime: 26 ms
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = collections.deque()  
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        q = self._queue
        q.append(x)
        [q.append(q.popleft()) for _ in range(len(q)-1)]
        
        
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self._queue.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._queue[0]
    
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not len(self._queue)

    
    
    

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
