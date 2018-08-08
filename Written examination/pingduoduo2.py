import sys

def isval(s):
    if s.__contains__('.'):
        if s.index('.')!=1 and s[0]=='0' and s[1]=='0':
            return False
        if s[-1]=='0':
            return False
    else:
        if s[0]=='0':
            return False
    if s[0]=='.' or s[-1]=='.':
        return False
    return True

def addpoint(s):
    ans = set()
    length = len(s)
    for i in list(range(1,length)):
        lefts = s[:i]
        rights = s[i:]
        news = ''.join(lefts)+'.'+''.join(rights)
        if isval(news):
            ans.add(news)
    if isval(s):
        ans.add(s)
    if s=='0':
        ans.add(s)
    return ans

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    length = len(line)
    ans = []
    for i in list(range(1,length)):
        lefts = line[:i]
        rights = line[i:]
        leftset = addpoint(lefts)
        rightset = addpoint(rights)
        for ls in leftset:
            for rs in rightset:
                try:
                    ls = int(ls)
                except:
                    ls = float(ls)

                try:
                    rs = int(rs)
                except:
                    rs = float(rs)
                ans.append([ls,rs])
    print(len(ans))
    print(ans)