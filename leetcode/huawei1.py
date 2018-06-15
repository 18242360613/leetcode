#coding=utf-8
import sys

if __name__ == "__main__":
    while True:
        line = sys.stdin.readline().strip()
        if line=='':
            break
        maxstr=""
        maxlen=0
        maxi = 0
        length = len(line)
        i=0
        while i < length:
            if line[i]<='9' and '0'<=line[i]:
                j = i
                while j<length and (line[j]<='9' and '0'<=line[j]):
                    j+=1
                if j-i >=maxlen:
                    maxlen = j-i
                    maxstr = line[i:j]
                i  = j
            i+=1
        # print("%s,%d" % (maxstr, maxlen))
        if maxlen>0:
            print("%s,%d"%(maxstr,maxlen))
        else:
            print("\"\",0")
