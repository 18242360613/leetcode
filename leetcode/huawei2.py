#coding=utf-8
import sys

if __name__ == "__main__":
    nums2bit=['0000','0001','0010','0011',
              '0100','0101','0110','0111',
              '1000','1001','1010','1011',
              '1100','1101','1110','1111']
    nums16 = ['0','1','2','3',
              '4','5','6','7',
              '8','9','A','B',
              'C','D','E','F']
    while True:
        N = sys.stdin.readline().strip()
        if N=='':
            break
        bits = sys.stdin.readline().strip().split()
        M = int(sys.stdin.readline().strip())
        bitnums = []
        for i in range(M):
            bitnums.append(int(sys.stdin.readline().strip()))
        strbit = ""
        for s in bits:
            for c in s[2:]:
                indexx = nums16.index(c)
                strbit=strbit+nums2bit[indexx]
        start=0
        for i in bitnums:
            numbit = strbit[start:start+i]
            start+=i
            print(int(numbit,2))