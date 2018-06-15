class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pastsl,paths = [p for p in path.split("/") if p],[]
        for p in pastsl:
            if p=='.': continue
            if p=="..":
                if len(paths)>0:
                    paths.pop()
            else: paths.append(p)

        return "/"+"/".join(paths)

s = Solution()
ans = s.simplifyPath("/..")
print(ans)