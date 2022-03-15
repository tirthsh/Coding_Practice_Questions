'''
Hash Table

key         value
Jan         [{1: 27} -> {2: 31} -> {3: 23}]
Feb         [{1: 22} -> {2: 28}]
Mar         []
'''

'''
Exercise: nyc_weather_data.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
1. What was the average temperature in first week of Jan
2. What was the maximum temperature in first 10 days of Jan
3. What was the temperature on Jan 9?
4. What was the temperature on Jan 4?
'''

from csv import DictReader
import codecs

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, new_node):
        tmp = self.head

        #make new node head if linked list is empty
        if tmp == None:
            self.head = new_node
            return
        else:
            #append new node to end
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = new_node
        return
    
    def find_temp(self, day):
        tmp = self.head

        while tmp != None:
            data = tmp.data
            if data.keys()[0] == day:
                return data[day]
            tmp = tmp.next
        return 
    
    
    def helper_retrieve_data(self):
        tmp = self.head
        data = []
        
        while tmp != None:
            data.append(tmp.data)
            tmp = tmp.next
        
        return data
    
class HashTable:
    def __init__(self):
        self.MAX = 12
        self.list = [[] for i in range(self.MAX)]
    
    #hash function: h(month_name) = month_num
    def hash_function(self, key):
        mapping = {"Jan": 0, "Feb": 1, "Mar": 2, "Apr": 3, "May": 4, "June": 5, "July": 6, "Aug": 7, "Sep": 8, "Oct": 9, "Nov": 10, "Dec": 11}
        return mapping[key]
    
    def add_value(self, month, day, temp):
        data = {day: temp}
        index = self.hash_function(month)

        #create new node
        new_node = Node(data)

        list_of_tmps = self.list[index]

        if len(list_of_tmps) == 0:
            linked_list = LinkedList()
        else:
            linked_list = list_of_tmps[0]
        
        linked_list.add_node(new_node)
        self.list[index] = [linked_list]
    
    def is_present(self, month, day):
        pass
    
    def find_temp(self, month, day):
        index = self.hash_function(month)
        list_of_tmps = self.list[index]

        if len(list_of_tmps) == 0:
            return 
        else:
            linked_list = list_of_tmps[0]
            temp = linked_list.find_temp(day)
            return temp
    
    def find_avg_temp(self, month, range_in_days):
        total_temp = 0
        for i in range(1, range_in_days+1):
            temp = int(self.find_temp(month, str(i)))
            total_temp += temp
            print(i)
            print(total_temp)
        
        print(total_temp)
        return total_temp / range_in_days
    
    def find_max_temp(self, month, range_in_days):
        max_temp = float('-inf')
        for i in range(1, range_in_days+1):
            temp = int(self.find_temp(month, str(i)))
            if temp > max_temp:
                max_temp = temp
        
        return max_temp

    def print_hash_table(self):
        for each_list in self.list:
            if len(each_list) == 0:
                print([])
            else:
                linked_list = each_list[0]
                data = linked_list.helper_retrieve_data()
                print(data)
        print()

def read_csv(file_path):
    # open file in read mode
    with open(file_path, 'r') as read_obj:
        data = []
        # pass the file object to reader() to get the reader object
        csv_reader = DictReader(codecs.EncodedFile(read_obj, 'utf-8', 'utf-8-sig'))
        header = next(csv_reader)

        #skip header
        if header != None:
            # Iterate over each row in the csv using reader object
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                data.append(row)
    
    return data

if __name__ == "__main__":
    #file_path = "/Users/tirthshah/Desktop/Github/Coding_Practice_Questions/hash/nyc_weather_data.csv"
    #data = read_csv(file_path)
    data = [
        {'Temperature': '22', 'Day': '1', 'Month': 'Jan'}, 
        {'Temperature': '22', 'Day': '2', 'Month': 'Jan'},
        {'Temperature': '22', 'Day': '3', 'Month': 'Jan'},
        {'Temperature': '22', 'Day': '4', 'Month': 'Jan'},
        {'Temperature': '22', 'Day': '5', 'Month': 'Jan'},
        {'Temperature': '22', 'Day': '6', 'Month': 'Jan'},
        {'Temperature': '22', 'Day': '7', 'Month': 'Jan'},
        {'Temperature': '32', 'Day': '8', 'Month': 'Jan'},
        {'Temperature': '22', 'Day': '9', 'Month': 'Jan'},
        {'Temperature': '22', 'Day': '10', 'Month': 'Jan'}
    ]
    print(data)

    hash_table_obj = HashTable()

    for each_val in data:
        month = each_val["Month"]
        day = each_val["Day"]
        temp = each_val["Temperature"]

        #add to hash table
        hash_table_obj.add_value(month, day, temp)
    
    #hash_table_obj.print_hash_table()

    temp = hash_table_obj.find_temp('Jan', '4')
    print(temp)

    avg_temp = hash_table_obj.find_avg_temp('Jan', 7)
    print(avg_temp)

    max_temp = hash_table_obj.find_max_temp('Jan', 7)
    print(max_temp)
