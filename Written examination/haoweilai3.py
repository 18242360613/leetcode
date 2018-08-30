import sys
import copy

def dfs(opnums,cur,end,temps,ans):
    if cur == end:
        ans.append(copy.deepcopy(temps))
        return

    temps.append(opnums[cur])
    dfs(opnums,cur+1,end,temps,ans)
    temps.pop()
    dfs(opnums,cur+1,end,temps,ans)

if __name__ == '__main__':
    nums,opnums,renums,end = [int(num) for num in sys.stdin.readline().strip().split()],[],[],0
    for i in range(len(nums)):
        if nums[i]==0:
            end = end + 1
            opnums.append(i)
        else:
            renums.append(i)
    ans,finalans = [],[]
    dfs(opnums,0,end,[],ans)
    for ops in ans:
        if len(ops)==0:
            ops = renums
        else:
            ops.extend(renums)
        ops.sort()
        tmpstr = ""
        for num in ops:
            tmpstr = tmpstr+str(num)
        finalans.append(tmpstr)
    finalans.sort()
    for numlist in finalans:
        print(numlist)