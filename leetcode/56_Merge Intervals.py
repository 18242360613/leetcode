# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals,key=lambda x:x.start)
        ans = []
        for inter in intervals:
            if not ans or ans[-1].end < inter.start:
                ans.append(inter)
            else:
                ans[-1].end = max(inter.end,ans[-1].end)
        return ans

s = Solution()
intervals = [Interval(1,4),Interval(2,3)]
ans = s.merge(intervals)
for a in ans:
    print(a.start,a.end)