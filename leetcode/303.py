class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.length = len(nums)
        self.sums = [[0] * self.length]
        if self.length != 0:
            self.sums[0] = nums[0]
            for i in list(range(1, self.length)):
                self.sums[i] = self.sums[i - 1] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > j:
            return 0
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i - 1]



        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)
obj = NumArray([-2,0,3,-5,2,-1])
param_1 = obj.sumRange(0,2)