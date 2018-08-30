# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        maxnum = 0
        for p1 in points:
            slopedict,duplicate = {},1
            for p2 in points:
                if p1.x == p2.x and p1.y == p2.y:
                    if p1 == p2:
                        continue
                    duplicate+=1
                    continue
                if p1.x == p2.x: slope = float("inf")
                else:
                    slope =(((p1.y -p2.y)*1000000000000000)/(p1.x-p2.x))

                if slope in slopedict:
                    slopedict[slope] = slopedict.get(slope)+1
                else:
                    slopedict[slope]=1

            if len(slopedict.keys())==0:
                maxnum = duplicate
            else:
                for key in slopedict.keys():
                    if slopedict[key]+duplicate>maxnum:
                        maxnum = slopedict[key]+duplicate

            slopedict.clear()
        return maxnum

# [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# [[0,0],[94911151,94911150],[94911152,94911151]]
p1 = Point(0,0)
p2 = Point(94911151,94911150)
p3 = Point(94911152,94911151)
# p4 = Point(4,1)
# p5 = Point(2,3)
# p6 = Point(1,4)

points = [p1,p2,p3]
s = Solution()
ans = s.maxPoints(points)
print(ans)