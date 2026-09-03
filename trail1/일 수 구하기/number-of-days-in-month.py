n = int(input())
if n == 2:
    print("28") 
elif n < 8 and n%2 == 0 or n >= 8 and n%2 != 0:
    print("30")
else:
    print("31")
