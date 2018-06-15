class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pair = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in ('(','[','{'):
                stack.append(c)
            else:
                if len(stack)>0 and c==pair[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0

s = Solution()
print(s.isValid('[])'))