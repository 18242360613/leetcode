#coding=utf-8
import sys

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    N,M = int(line.split(" ")[0]),int(line.split(" ")[1])
    numa = [int(num) for num in sys.stdin.readline().strip().split()]
    numb = [int(num) for num in sys.stdin.readline().strip().split()]
    numa.sort()
    numb.sort()
    suma = sum(numa)
    sumb = sum(numb)
    lena = len(numa)
    lenb = len(numb)
    meana = suma / lena
    meanb = sumb / lenb

    if meana == meanb:
        print(0)
    else:
        if meana < meanb:
            meana,meanb = meanb,meana
            numa,numb = numb,numa
            suma,sumb = sumb,suma
            lena,lenb = lenb,lena

        indexb = 0
        for i in range(lena):
            if numa[i]>meanb:
                indexb = i
                break
        result = 0
        while meanb < meana:
            if not numa[indexb] in numb:
                suma = suma-numa[indexb]
                lena = lena -1
                meana = suma/lena
                sumb = sumb+numa[indexb]
                lenb = lenb +1
                meanb = sumb/lenb
                result+=1
            indexb+=1
        print(result)


