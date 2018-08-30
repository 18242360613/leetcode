class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for s in tokens:
            if s not in ["+", "-", "*", "/"]:
                stack.append(int(s))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if s == '+':
                    result = num1 + num2
                elif s == '-':
                    result = num1 - num2
                elif s == '*':
                    result = num1 * num2
                else:
                    result = num1 / num2
                stack.append(int(result))
        return stack[-1]

s = Solution()
ans = s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(ans)