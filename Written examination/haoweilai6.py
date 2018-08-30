import sys
if __name__ == '__main__':
    original = sys.stdin.readline().strip()
    old = sys.stdin.readline().strip()
    new = sys.stdin.readline().strip()
    print(original.replace(old,new))