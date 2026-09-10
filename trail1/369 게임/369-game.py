n = int(input())

def isthere369(n):
    s = str(n)

    rt = 0

    for i in range(len(s)):
        if s[i] == '3' or s[i] == '6' or s[i] == '9':
            rt = 1

    return rt

i = 1

while i < n + 1:
    if i % 3 == 0 or isthere369(i):
        print(0, end=" ")
    else:
        print(i, end=" ")

    i += 1