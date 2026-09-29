a, b, c = map(int, input().split())

boolean = False
for i in range(a, b+1):
    if i%c == 0:
        boolean = True

if boolean:
    print("YES")
else:
    print("NO")