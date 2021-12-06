t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    m = {}
    answer = 0
    for i in range(n):
        x = nums[i] - i
        if not x in m:
            m[x] = 1
        else:
            answer += m[x]
            m[x] += 1

    print(answer)

