# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ans,i = [],0
        while i < len(intervals) and newInterval.start > intervals[i].end:
            ans.append(intervals[i])
            i+=1

        while i< len(intervals) and newInterval.end >= intervals[i].start:
            newInterval = Interval(min(intervals[i].start,newInterval.start),
                                   max(intervals[i].end,newInterval.end)
                                   )
            i+=1
        ans.append(newInterval)

        while i<len(intervals):
            ans.append(intervals[i])
            i+=1
        return ans
s = Solution()
intervals = [Interval(1,3),Interval(6,9),Interval(10,11)]
ans = s.insert(intervals,Interval(2,5))
for a in ans:
    print(a.start,a.end)