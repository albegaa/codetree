cnt = 0
sum = 0

for _ in range(10):
    n = int(input())
    if n >= 0 and n <= 200:
        cnt += 1
        sum += n

avg = sum / cnt
print(f"{sum} {avg:.1f}")