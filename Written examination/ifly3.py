import sys
class shusu:
    def __init__(self):
        self.ss = [2]
        self.legth = 1
    def genss(self,k):
            a = self.ss[-1]+1
            while len(self.ss)<=k:
                b = False
                for b in self.ss:
                    if a % b == 0:
                        b = False
                        break
                    else:
                        b = True
                if b == True:
                    self.ss.append(a)
                a+=1


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    s = shusu()
    for i in range(N):
        k = int(sys.stdin.readline().strip())
        if k<=s.legth:
            print(s.ss[k-1])
        else:
            s.genss(k)
            print(s.ss[k - 1])