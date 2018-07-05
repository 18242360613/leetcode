class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p = m+n-1
        m,n = m-1,n-1
        while 0 <= m and 0 <= n:
            if nums1[m]>=nums2[n]:
                nums1[p] = nums1[m]
                m-=1
            else:
                nums1[p] = nums2[n]
                n-=1
            p-=1

        while n>=0:
            nums1[p] = nums2[n]
            n -= 1
            p -= 1

num1 = [0]
m = 0
num2 = [1]
n = 1
s = Solution()
s.merge(num1,m,num2,n)
print(num1)