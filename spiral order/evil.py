s="1,3,4,6,7"
black = [0]*8
for c in s.split(","):
    black[int(c)-1]=1
# 定义每次给前一半的人进行尝试
low,high =1,250
for i in range(8):
    mid = (low+high)//2
    if black[i] ==1:
        high = mid
    else:
        low = mid+1

print(low,high)