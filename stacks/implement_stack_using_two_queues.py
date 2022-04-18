class Stack:

    def __init__(self):
        self.push_queue = []
        self.pop_queue = []

    def push(self, x):
        self.push_queue.append(x)
    
    def pop(self):
        
    
    def peek(self):
        pass
    
    def isEmpty(self):
        return len(self.push_queue) == 0 and len(self.pop_queue) == 0

    def print_stack(self):
        print(self.push_queue + self.pop_queue)


stack = Stack()
