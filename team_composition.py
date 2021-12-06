t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a == b:
        print(a // 2)
        continue

    print(min(min(a, b), int((a + b) / 4)))

