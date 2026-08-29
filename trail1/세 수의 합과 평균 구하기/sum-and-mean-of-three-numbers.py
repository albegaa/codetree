arr = input().split()
i=0
for k in arr:
    arr[i] = int(arr[i])
    i += 1

print(sum(arr), (sum(arr)//len(arr)), sep="\n")