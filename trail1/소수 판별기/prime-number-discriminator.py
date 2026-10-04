N = int(input())

if N < 2:
    print("C")
else:
    is_prime = True

    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            is_prime = False
            break

    if is_prime:
        print("P")
    else:
        print("C")