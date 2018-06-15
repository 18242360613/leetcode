class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m,n = len(nums1),len(nums2)
        if m>n:
            nums1,nums2,m,n=nums2,nums1,n,m
        if n == 0:
            return 0.0
        imax,imin,halflen = m,0,(m+n+1)//2
        while imax >= imin:
            i = (imax+imin)//2
            j = halflen-i
            if i<m and nums1[i] < nums2[j-1]:
                imin=i+1
            elif i>0 and nums1[i-1] > nums2[j]:
                imax=i-1
            else:
                if i==0:
                    maxleft = nums2[j-1]
                elif j==0:
                    maxleft = nums1[i-1]
                else:
                    maxleft = max(nums1[i-1],nums2[j-1])

                if (m+n)%2==1:
                    return maxleft

                if i==m:
                    minright = nums2[j]
                elif j==n:
                    minright = nums1[i]
                else:
                    minright = min(nums1[i],nums2[j])
                return (minright+maxleft)/2.0





S = Solution()
result = S.findMedianSortedArrays([1,3],[2])
print(result)