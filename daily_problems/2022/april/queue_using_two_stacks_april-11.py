#queue -> FIFO

class Queue:

    '''
    Initiate two stacks 
    - pop_stack: 
        - will keep track of elements in queue order -> pop() and peek() will O(1)

    - push_stack:
        - append item on to this stack everytime push(x) is called -> push(x) will be O(1)
    '''
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
    
    '''
    Every time push(x) is called, append to push_stack
    '''
    def push(self, x):
        self.push_stack.append(x)

    '''
    If pop_stack is not empty, then simply access the top element of pop_stack
        - that should be first element of queue
    Otherwise, add all elements from push stack on to pop_stack and return top element in pop_stack
    '''
    def pop(self):
        if len(self.pop_stack) != 0:
            self.pop_stack.pop()
        else:
            while len(self.push_stack) != 0:
                self.pop_stack.append(self.push_stack.pop())

            self.pop_stack.pop()

    '''
    Same as pop, except dont pop top element of pop_stack, simply return it
    '''
    def peek(self):
        if len(self.pop_stack) != 0:
            return self.pop_stack[-1]
        else:
            while len(self.push_stack) != 0:
                self.pop_stack.append(self.push_stack.pop())
            
            return self.pop_stack[-1]

    '''
    If both the stacks are empty then queue is empty.
    '''
    def isEmpty(self):
        return len(self.pop_stack) == 0 and len(self.push_stack) == 0
    
    def print_queue(self):
        print(self.pop_stack + self.push_stack)

queue = Queue()
queue.push(4)
queue.push(0)
queue.push(1)
queue.print_queue()
print(queue.peek())
queue.pop()
queue.print_queue()
print(queue.peek())