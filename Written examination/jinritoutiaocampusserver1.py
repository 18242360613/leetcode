#coding=utf-8
import sys

if __name__ == "__main__":

    while True:
        line = sys.stdin.readline().strip()
        if line=="":
            break
        N,K = int(line.split()[0]),int(line.split()[1])
        nums = [int(num) for num in sys.stdin.readline().strip().split()]
        nums.sort()
        if K == 0:
            result = 0
            i = 0
            while i < N:
                j=i+1
                while j < N and nums[j]==nums[i]:
                    j+=1
                if j>i+1:
                    result+=1
                i = j
            print(result)
        else:
            result = 0
            nums = list(set(nums))
            nums.sort
            dirct={}
            for i in nums:
                if i-K in dirct:
                    result += 1
                dirct[i]=1
            print(result)
