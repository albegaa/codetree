n = int(input())

c = 0
h = 0
r = 0

for i in range(1, n+1):
    if i%12 == 0:
        r += 1
    elif i%3 == 0:
        h += 1
    elif i%2 == 0:
        c += 1

print(c, h, r)