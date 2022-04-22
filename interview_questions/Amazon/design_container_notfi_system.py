# Assume we are hosting a service that hosts and manages containers for the customers.
# To make sure the customer containers are running healthy, we have a cron job that reports the availability of the container.
# The cron job is supposed to report the availability of the container every 5 seconds, with the value of either 1 or 0 (1 being available, 0 being not available).
# Write a program to notify the customers whose containers are not available, using the collected data.

'''
Input -> 
Output -> informs customer that x list of containers are not running
Assumptions 
Edgecases
Algo:
    
Complexity
'''
from enum import ENUM

class ContainerStatus(ENUM):
    ON = 1
    OFF = 0


class Container:
    def __init__(self, name_of_container, customer_name, enum_val):
        self.status = enum_val
        self.name_of_container = name_of_container
        self.customer_name = customer_name
        self.failure_count = 0
        
    def getStatus(self):
        return self.status
    
    def setStatus(self, new_status):
        if self.status == 0 and new_status == 0:
            self.failure_count += 1
        
        if self.status == 1 and new_status == 0:
            self.failure_count = 1
        
        self.status = new_status

class Customer:
    def __init__(self, name, frequency_fail_count=1):
        self.name = name
        self.container_list = []
        self.frequency_fail_count = frequency_fail_count
        
    def notify(self):
        res = []
        
        for each_container in self.container_list:
            if each_container.status == 0:
                if each_container.failure_count >= self.frequency_fail_count:
                    res.append(each_container)
    
        if len(res) != 0:
            #notify
        
        #otherwise you dont need to notify because all containers are healthy
        
        


