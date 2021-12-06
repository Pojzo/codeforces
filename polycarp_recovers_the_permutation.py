t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    max_element = max(a)
    if max_element == a[0] or max_element == a[-1]:
        print(" ".join([str(x) for x in reversed(a)]))
    else:
        print(-1)
