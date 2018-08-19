# class Solution:
#     def candy(self, ratings):
#         """
#         :type ratings: List[int]
#         :rtype: int
#         """
#         candy = [1]*len(ratings)
#         for i in range(len(ratings)-1):
#             if ratings[i+1] > ratings[i]:
#                 candy[i+1] = candy[i]+1
#
#         for i in list(range(len(ratings)-2,-1,-1)):
#             if ratings[i] > ratings[i+1]:
#                 candy[i] = max(candy[i],candy[i+1]+1)
#         return sum(candy)

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings or len(ratings)==0:
            return 0
        start,i,length,sumv = 0,0,len(ratings),1
        while i < length-1:
            while i < length-1 and ratings[i] < ratings[i+1]:
                i+=1

            left = i - start
            start = i

            while i < length-1 and ratings[i] > ratings[i+1]:
                i+=1

            right = i - start
            start = i
            peak = max(left,right)+1
            sumv = sumv+(left+1)*left/2 + (right+1)*right/2+peak-1

            while i < length-1 and ratings[i] == ratings[i+1]:
                i+=1
                sumv+=1
            start = i

        return int(sumv)

s = Solution()
ans = s.candy([1,2,3,4,4,3,2,1])
print(ans)