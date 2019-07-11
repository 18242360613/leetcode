class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        quot = dict()
        ans = []
        if numerator * denominator < 0:
            ans.append('-')
            quot['-']=0
        numerator = abs(numerator)
        denominator = abs(denominator)
        frist,last,isfloat = 0,0,0
        while True:
            qu, re = divmod(numerator,denominator)
            ans.append(str(qu))
            if re > 0 and isfloat==0:
                ans.append(".")
                isfloat = 1

            if abs(re - 0) < 0.00000001:
                break

            if re in quot:
                frist = quot[re]
                last = len(ans)
                break
            else:
                quot[re] = len(ans)

            numerator = re * 10

        if frist > 0:
            restr = "".join(ans[:frist])
            restr = restr+"("+"".join(ans[frist:last])+")"
        else:
            restr = "".join(ans)

        return restr


S = Solution()
ans = S.fractionToDecimal(1,3)
print(ans)