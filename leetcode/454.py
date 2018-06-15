class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        if len(A) < 1:
            return 0
        
        results = 0
        tmpdir = {}
        for c in C:
            for d in D:
                if c+d in tmpdir:
                    tmpdir[c+d]+=1
                else:
                    tmpdir[c+d]=1
        for a in A:
            for b in B:
                if -(a+b) in tmpdir:
                    results+=tmpdir[-(a+b)]
        return results