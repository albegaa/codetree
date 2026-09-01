am, ae = map(int, input().split())
bm, be = map(int, input().split())

if am == bm and ae > be:
    print("A")
elif am == bm and ae < be:
    print("B")
elif am > bm:
    print("A")
else: print("B")