a, b = map(int, input().split())

s = a // b
r = a % b

print(s, ".", sep="", end="")

for _ in range(20):
    r *= 10
    print(r // b, end="")
    r %= b