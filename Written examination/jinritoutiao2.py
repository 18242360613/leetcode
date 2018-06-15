#coding=utf-8
import sys

global mino

if __name__ == "__main__":

    def oper(s, m, i, j, n):
        global mino
        if s == n:
            if mino > i + j:
                mino = i + j
        elif s < n:
            oper(s * 2, s, i + 1, j, n)
            oper(s + m, m, i + 1, j, n)

    while True:
        N = sys.stdin.readline().strip()
        if N=="":
            break
        N = int(N)
        global mino
        mino = 100000
        oper(1, 1, 0, 0, N)
        print(mino)