n = int(input())

boolean = False
for i in range(2, n):
    if n%i == 0:
        boolean = True

if boolean:
    print("C")
else:
    print("N")