'''
You have installed a new tracking system in your local shop. The system tracks every time a customer enters or exits the shop. Now you'd like to test if the system works correctly.

At the beginning and at the end of the day there are no customers in the shop. The system logs all the in and out movements of customers in a two-dimensional array of strings events, where events[i][0] is the unique id of the customer entering or exiting the shop, and events[i][1] is either "in" or "out", depending on the direction of movement of that customer.

Your task is to write a function solution(events), which returns true if the system may have worked correctly, and false otherwise.

Example:
events = [
  ["John_0", "in"],
  ["Mary_0", "in"],
  ["John_0", "out"],
  ["Mary_0", "out"]
]
the output should be solution(events) = true.

events = [
  ["John_0", "in"],
  ["John_0", "in"],
  ["John_0", "out"],
  ["John_0", "out"]
]
the output should be solution(events) = false.

The same person cannot enter the shop twice without exiting.

events = [
  ["John_0", "in"],
  ["John_1", "in"],
  ["John_1", "out"]
]
the output should be solution(events) = false.

'''


def solution(events):
    '''
    input -> 2d array 
    output -> boolean if system worked or not
    '''
    
    stack = []
    works = True
    
    if events == None or len(events) == 0:
        return True
    
    for i in range(0, len(events)):
        person = events[i][0]
        activity = events[i][1]
        
        if activity == "in":
            if person not in stack:
                stack.append(person)
            else:
                works = False
                break
        else:
            if person in stack:
                stack.remove(person)
            else:
                works = False
                break
    
    return len(stack) == 0 or works
        
        
        
            

