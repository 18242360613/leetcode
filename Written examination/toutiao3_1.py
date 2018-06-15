import sys

if __name__ == "__main__":
    i = 0
    while True:
        if i==0:
            line = sys.stdin.readline().strip()
        else:
            line1 = sys.stdin.readline()
            if line1=="":
                break
            line = sys.stdin.readline().strip()
        if line == "":
            break
        M,N = int(line.split(" ")[0]),int(line.split(" ")[1])
        st,k = [],[]
        for i in range(M):
            line = sys.stdin.readline().strip()
            st.append(line)
        sys.stdin.readline().strip()

        for i in range(N):
            key = sys.stdin.readline().strip()
            k.append(key)

        for key in k:
            ans=-1
            for s in st:
                if key[:len(s)]==s:
                    ans = 1
                    break
                elif key<s:
                    break
            print(ans)
        print()
        i+=1
        line=""