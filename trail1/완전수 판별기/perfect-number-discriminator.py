n = int(input())

if n == 1:
    print("N")
else:
    total = 1

    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i

            if i != n // i:
                total += n // i

        i += 1

    if total == n:
        print("P")
    else:
        print("N")