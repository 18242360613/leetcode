import os
import sys

def inverse_number(nums):
    ans = 0
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] > nums[i]:
                ans += 1
    return ans

if __name__ == '__main__':
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        nums = [int(i) for i in  line.split(" ")][1:]
        ans = inverse_number(nums)
        print(ans)