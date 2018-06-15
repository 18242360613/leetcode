import sys

if __name__ == "__main__":
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        if len(line)<=3:
            print(4)
        else:
            print(5)