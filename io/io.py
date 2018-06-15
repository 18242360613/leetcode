#先向文件写入N,再写入N行随机数
import random


def write2file(strcont):
    file = open("input.txt","a+")
    file.write(strcont)

def readfromfile():
    file = open("input.txt", "r")
    N = int(file.readline().strip())
    for i in range(N):
        print(file.readline().strip())

# result = random.randint(1,10)
# write2file(str(result))
readfromfile()