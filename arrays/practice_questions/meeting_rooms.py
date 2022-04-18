'''
Given an array of meeting time intervals consisting of start and 
end times[[s1,e1],[s2,e2],...](si< ei), determine if a person could attend all meetings.
'''

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:

    '''
    Idea is to sort meetings by start time.
    Then check if any of the end time is after any of the start time of next meeting
    '''

    #meeting rooms = [[0,30],[5,10],[15,20]]
    def canAttendMeetings(self, intervals):
        if not intervals or len(intervals) == 0:
            return True
        
        #sort by start time
        #will take nlog(n)
        intervals.sort(key=lambda each_interval: each_interval.start)

        for i in range(1, len(intervals)):
            previous_meeting = intervals[i-1]
            current_meeting = intervals[i]

            if current_meeting.start < previous_meeting.end:
                return False
            
        return True

interval1 = Interval(0, 30)
interval2 = Interval(5,10)
interval3 = Interval(15,20)

intervals = []
intervals.append(interval1)
intervals.append(interval2)
intervals.append(interval3)

solution = Solution()
print(solution.canAttendMeetings(intervals))
