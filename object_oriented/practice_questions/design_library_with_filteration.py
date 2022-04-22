from enum import Enum
from abc import ABC, abstractmethod

class FileNameOperators(Enum):
    EQUAL="=="
    NOT_EQUAL="!="

class FileSizeOperators(Enum):
    EQUAL="=="
    NOT_EQUAL="!="
    LESS_THAN="<"
    GREATER_THAN=">"
    LESS_THAN_EQUAL_TO="<="
    GREATER_THAN_EQUAL_TO=">="

class Filter:
    def __init__(self, value, operation):
        self.value = value
        self.operation = operation

class File:
    def __init__(self, file_name, size):
        self.file_name = file_name
        self.size = size

class Library:
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity
        self.files = []
    
    def add_file(self, file_obj):
        if self.count < self.capacity:
            self.files.append(file_obj)
            self.count += 1
        else:
            raise Exception("Sorry, library is full. Cannot add any more files.")
        
    def remove_file(self, file_obj):
        if file_obj in self.files:
            self.files.remove(file_obj)
        else:
            raise Exception("This file does not exist in the library, cannot remove.")

    #list_of_filename_filters = [{"value": "foo.py", "operation": FileNameOperators.EQUAL}, {"value": "xyz", "operation": FileNameOperators.NOT_EQUAL}]
    #list_of_filesize_filters = [{"value": 25, "operation": FileSizeOperators.LESS_THAN}, {"value": 1, "operation": FileSizeOperators.NOT_EQUAL}]
    def filter(self, list_of_filename_filters=[], list_of_filesize_filters=[]):
        file_res = []
        size_res = []
        final_res = []
        filter_on = self.files

        #if no filter added, return all files
        if len(list_of_filename_filters) and len(list_of_filesize_filters) == 0:
            return self.files

        #{"value": "foo.py", "operation": FileNameOperators.EQUAL}
        for each_filter in list_of_filename_filters:
            #each_file: {"file_name": "foo.py", "size": 25}
            for each_file in filter_on:
                #foo.py == foo.py
                if eval(each_file.file_name each_filter[operation] each_filter.value):
                    file_res.append(each_file)

        #{"value": 25, "operation": FileSizeOperators.LESS_THAN}
        for each_fiter in list_of_filesize_filters:
            #each_file: {"file_name": "foo.py", "size": 25}
            for each_file in filter_on:
                if eval(each_file.size each_filter[operation] each_filter.value):
                    size_res.append(each_file)
        
        if len(file_res)==0 and len(size_res) == 0:
            return []
        
        if len(file_res) != 0 and len(size_res) != 0:
            return file_res
        
        if len(size_res) != 0 and len(file_res) == 0:
            return size_res

        #if both are not empty, find common elements
        final_res = list(set(file_res).intersection(size_res))

        return final_res








    