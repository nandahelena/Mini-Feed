o1, p1, b1 = map(int, input().split())
o2, p2, b2 = map(int, input().split())

if o1 > o2:
    print("A")
elif o2 > o1:
    print("B")
elif o1 == o2:
    if p1 > p2:
        print("A")
    if p2 > p1:
        print("B")
    if p2 == p1:
        if b1 > b2:
            print("A")
        if b2 > b1:
            print("B")