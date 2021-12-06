t = int(input())
for i in range(t):
    x, n = map(int, input().split())
    for i in range(1, n + 1):
        if x % 2 == 0:
            x -= i
        else:
            x += i

    print(x)
