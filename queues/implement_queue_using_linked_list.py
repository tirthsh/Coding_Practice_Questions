#queue -> FIFO

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, node):
        if self.head == None:
            self.head = node 
        else:
            #add to end since FIFO
            #this way we can keep O(1) for peek() and pop()
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            
            tmp.next = node

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
            return 
        
        print("Peeking: " + str(self.head.val))
        return self.head.val
    
    def isEmpty(self):
        return self.size == 0

    def print_queue(self):
        queue = []
        if self.head != None:
            tmp = self.head
            while tmp != None:
                queue.append(tmp.val)
                tmp = tmp.next
        
        print(queue)

node1 = Node(4)
node2 = Node(0)
node3 = Node(3)

queue = Queue()
queue.push(node1)
queue.push(node2)
queue.push(node3)
queue.print_queue()

queue.peek()
queue.pop() #remove 4
queue.print_queue()

queue.pop() # remove 0
queue.print_queue()

queue.pop() # remove 3

queue.print_queue()
