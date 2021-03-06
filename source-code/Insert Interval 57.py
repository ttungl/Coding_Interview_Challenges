# 57. Insert Interval
# ttungl@gmail.com
# Given a set of non-overlapping intervals, insert a new interval into the intervals 
# (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
   
   
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # sol 1:
        # runtime: 73ms
        i, res = 0, []
        s, e = newInterval.start, newInterval.end
        # insert
        while i < len(intervals) and s > intervals[i].end: 
            res += intervals[i], 
            i += 1
        # merge
        while i < len(intervals) and e >= intervals[i].start:
            s, e = min(s, intervals[i].start), max(e, intervals[i].end)
            newInterval = Interval(s, e)
            i += 1
        res += newInterval,
        res += intervals[i:]
        return res
    
        # sol 2:
        # key: use left and right list for non-overlap pairs.
        # for every pair in the list
        # if input start > current end: add to left,
        # if current start > input end: add to right,
        # else, merging and update: input start, end = min(starts), max(ends)
        # return left +[s,e]+right
        # runtime: 69ms
        s, e = newInterval.start, newInterval.end
        left, right = [], []
        for i in intervals:
            if s > i.end:
                left += i,
            elif i.start > e:
                right += i,
            else: # merge
                s, e = min(s, i.start), max(e, i.end)
        return left + [Interval(s, e)] + right
        
            








