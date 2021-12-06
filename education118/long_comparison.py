t = int(input())
for i in range(t):
    x1, p1 = map(int, input().split())
    x2, p2 = map(int, input().split())
    min_p = min(p1, p2)
    p1 -= min_p
    p2 -= min_p
    if p1 >= 7:
        print(">")
    elif p2 >= 7:
        print("<")
    else:
        x1 *= 10 ** p1
        x2 *= 10 ** p2
        if x1 > x2:
            print(">")
        elif x1 < x2:
            print("<")
        else:
            print("=")

