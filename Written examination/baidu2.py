import sys

if __name__ == "__main__":

    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        upnum = 0
        for c in line:
            if c.isupper():
                upnum+=1
        if upnum > len(line)//2:
            print(line.upper())
        else:
            print(line.lower())