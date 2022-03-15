'''
You are given two linked-lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 

Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

'''
Input -> two linked lists
Output -> a single linked lists of their sum
Assumptions -> non-negative integers
Edge Cases -> 
Example -> 1 -> 2 -> 3 + 3 -> 2 -> 1 = 321 + 123 = 444 -> 4 -> 4 -> 4
Algo -> Reverse the list, get the number values, sum them and create a new LL from the sum calculated
Complexity -> Time: O(n), Space: O(n)
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    #append new node to end of LL
    def add(self, new_node):
        tmp = self.head
        
        if tmp == None:
            self.head = new_node
            return
        
        while tmp.next != None:
            tmp = tmp.next
        
        tmp.next = new_node
    
    #reverse func needed as initial LL given in reverse order
    def reverse_linked_list(self):
        tmp = self.head

        if tmp == None or tmp.next == None:
            return tmp
        
        prev = None
        while tmp != None:
            next_node = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = next_node
        
        self.head = prev
        return self.head
    
    #main method
    #takes another linked list
    def add_two_linked_list(self, another_linked_list):
        #reverse both linked lists to get actual number
        self.reverse_linked_list()
        another_linked_list.reverse_linked_list()

        #get the number of each
        num1 = self.get_num()
        num2 = another_linked_list.get_num()

        #add the two nums
        sum = num1 + num2

        #create a new linked list from the sum calculated
        summation_linked_list = LinkedList()
        for each_num in str(sum):
            new_node = Node(int(each_num))
            summation_linked_list.add(new_node)
        
        return summation_linked_list
    
    #get the number as int given a LL where each node's value is an int
    def get_num(self):
        tmp = self.head
        num = ""
        if tmp == None:
            return
        
        while tmp != None:
            num += str(tmp.data)
            tmp = tmp.next
        
        return int(num)

    #helper to print LL
    def print_list(self):
        tmp = self.head 

        while tmp != None:
            print(str(tmp.data) + " -> ", end = "")
            tmp = tmp.next

        print("None")
        print()
    
linked_list1 = LinkedList()
linked_list2 = LinkedList()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

linked_list1.add(node1)
linked_list1.add(node2)
linked_list1.add(node3)

linked_list1.print_list()

node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

linked_list2.add(node4)
linked_list2.add(node5)
linked_list2.add(node6)

linked_list2.print_list()

new_linked_list = linked_list1.add_two_linked_list(linked_list2)
new_linked_list.print_list()

