import sys

def find_num_of_same(str1, str2):
    friend1 = str1.split()
    friend2 = str2.split()
    if str(user_id) in friend2:
        return 0
    else:
        number = len([x for x in friend1 if x in friend2])
        return number

if __name__ == '__main__':
    data = []
    info = ""
    string = sys.stdin.readlines()

    for i in range(len(string)):
        if i == 0:
            info = string[i]
        else:
            data.append(string[i])

    total_num = int(info.split(" ")[0])
    user_id = int(info.split(" ")[1])

    num = []
    for i in range(total_num):
        if i == user_id:
            num.append(0)
            continue
        else:
            num.append(find_num_of_same(data[user_id],data[i]))

    max_number = max(num)
    if max_number == 0:
        print(-1)
    else:
        print(num.index(max(num)))