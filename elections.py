t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())

    a2 = max(b, c)
    if a > a2:
        a2 = 0
    else:
        a2 = a2 - a + 1

    b2 = max(a, c)
    if b > b2:
        b2 = 0
    else:
        b2 = b2 - b + 1

    c2 = max(a, b)
    if c > c2:
        c2 = 0
    else:
        c2 = c2 - c + 1

    print(a2, b2, c2)
