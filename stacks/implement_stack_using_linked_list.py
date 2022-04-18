class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

'''
stack order = [top of stack ..... end of stack]
reason why this order so we can have pop() and peek() with time complexity as O(1)
'''    


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, node):
        if self.head == None:
            self.head = node
        else:        
            tmp = self.head
            node.next = tmp
            self.head = node
        
        print("Pushed: " + str(node.val))
        self.size += 1
    
    def pop(self):
        if self.head == None:
            return None
        
        tmp = self.head
        new_head = tmp.next
        self.head = new_head
        
        self.size -= 1
        print("Removed: " + str(tmp.val))
        return tmp.val

    def peek(self):
        if self.head == None:
            return None
        
        print("Peeking: " + str(self.head.val))
        return self.head.val
    
    def isEmpty(self):
        return self.size == 0
    
    def print_stack(self):
        stack = []
        if self.head != None:
            tmp = self.head

            while tmp != None:
                stack.append(tmp.val)
                tmp = tmp.next
        
        print(stack)

node1 = Node(4)
node2 = Node(0)
node3 = Node(3)

stack = Stack()
stack.push(node1)
stack.push(node2)
stack.push(node3)

stack.print_stack()

stack.peek()

stack.pop()
stack.print_stack()

stack.pop()
stack.print_stack()

stack.pop()
stack.print_stack()