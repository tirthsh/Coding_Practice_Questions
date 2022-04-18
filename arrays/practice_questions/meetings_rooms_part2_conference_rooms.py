#https://aaronice.gitbook.io/lintcode/sweep-line/meeting-rooms-ii

'''
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), 
find the minimum number of conference rooms required.

Input: [[0, 30],[5, 10],[15, 20]] -> [0,30], [5,10], [15,20]
Output: 2

Input: [[7,10],[2,4]]
Output:1

'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals or len(intervals) == 0:
            return 0
        
        num_of_meetings = 0
        intervals.sort(key=lambda each_interval: each_interval.start)

        #use minheap
        

