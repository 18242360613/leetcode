class Solution:
    def twoSum(self, numbers, target: int):
        a, b, = 0, len(numbers) - 1
        while a < b:
            s = numbers[a]+numbers[b]
            if s==target:
                return [a+1,b+1]
            elif s > target:
                b-=1
            elif s < target:
                a+=1
        return []

s = Solution()
ans = s.twoSum([5,5,6],11)
print(ans)