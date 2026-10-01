a, b = map(int, input().split())

boolean = False

for i in range(a, b + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        boolean = True

print(1 if boolean else 0)