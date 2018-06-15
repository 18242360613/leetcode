import sys

if __name__ == "__main__":

    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        length = len(line)
        l=length//2
        while l > 0:
            _, rem = divmod(length, l)
            if rem:
                l -= 1
                continue
            success = True
            for i in range(length):
                if line[i]!=line[i%l]:
                    success = False
                    break
            if success:
                break
            l -= 1
        if l>0:
            print(line[:l])
        else:
            print("false")