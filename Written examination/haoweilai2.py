import sys
if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for i in range(T):
        line = sys.stdin.readline().strip().split()
        x, k,c,y = int(line[0]), int(line[1]),0,1
        while c < k:
            if x+y == x|y:
                c+=1
            if c == k:
                break
            y+=1
        print(y)

# # define Max 2000
# int TheNum(int x, int k)
# {
#     int num = 0;
#     long i = 1;
#     for(;i < Max; i++)
#     {
#         if(num <k && ((x + i) == (x | i)))
#         {
#             num++;
#         }
#         if(num == k)
#         {
#             break;
#         }
#     }
#     return i;
# }
#