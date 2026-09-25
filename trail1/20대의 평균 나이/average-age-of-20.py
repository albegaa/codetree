cnt = 0
sum = 0
while True:
    n = int(input())
    if n > 29 or n < 20:
        avg = sum/cnt
        print(f"{avg:.2f}")
        break
    else:
        cnt += 1
        sum += n