class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        total,start,minleft = 0,0,float("inf")

        for i in range(len(gas)):
            total = total + gas[i] - cost[i]
            if total < minleft:
                minleft = total
                start = (i+1)%len(gas)

        return -1 if total<0 else start

s = Solution()
ans = s.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])
print(ans)