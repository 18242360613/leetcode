import sys

def getLongestUnRepeatedSubStr(s):
    charset = set()
    maxlen,curlen,curindex,maxindex,start,length = 0,0,0,0,0,len(s)
    while curindex < length:
        if s[curindex] in charset:
            if curlen > maxlen:
                maxlen = curlen
                maxindex = start
            while s[start]!=s[curindex]:
                charset.remove(s[start])
                start=start+1
                curlen=curlen-1
            start=start+1
        else:
            curlen+=1
            charset.add(s[curindex])
        curindex+=1

    if curlen > maxlen:
        maxlen = curlen
        maxindex = start
    return s[maxindex:maxindex+maxlen]

if __name__ == '__main__':
    # while True:
    #     line = sys.stdin.readlines().strip().split()
    #     if line==None:
    #         break
    #     print(getLongestUnRepeatedSubStr(line))
    print(getLongestUnRepeatedSubStr("abcdbbf"))