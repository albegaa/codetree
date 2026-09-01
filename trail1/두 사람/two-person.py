arr_A = input().split()
arr_B = input().split()

aa = int(arr_A[0])
sa = arr_A[1]
ab = int(arr_B[0])
sb = arr_B[1]

if (sa == 'M' and aa >= 19 or sb == 'M' and ab >= 19):
    print(1)
else:
    print(0)