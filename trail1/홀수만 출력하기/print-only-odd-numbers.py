n = int(input())

for _ in range(n):
    N = int(input())
    if N%2 != 0 and N%3 == 0:
        print(N)