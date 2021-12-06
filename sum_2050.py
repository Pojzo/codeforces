t = int(input())
for i in range(t):
    n = int(input())
    ln = len(str(n)) - 4

    if n == 2050:
        print(1)
        continue
    if n < 2050:
        print(-1)
        continue

    closest = 2050 * 10 ** ln
    if closest > n:
        closest //= 10

    answer = 0
    while n != 0:
        x = n // closest
        answer += x
        n -= x * closest
        closest //= 10
        if closest < 2050:
            break

    if n == 0:
        print(int(answer))
    else:
        print(-1)

