p1 = input().split()
p2 = input().split()
p3 = input().split()

lis = [p1, p2, p3]

cnt = 0
for i in range(3):
    if lis[i][0] == 'Y' and int(lis[i][1]) >= 37:
        cnt += 1

if cnt >= 2:
    print("E")
else:
    print("N")