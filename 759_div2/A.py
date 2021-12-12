t = int(input())
for i in range(t):
    n = int(input())
    height = 1
    nums = list(map(int, input().split()))
    not_watered = 0
    died = False
    for x in range(n):
        if nums[x] == 0:
            if not_watered == 1:
                died = True
                break
            else:
                not_watered += 1
        else:
            not_watered = 0
            if x >= 1 and nums[x - 1] == 1 and nums[x] == 1:
                height += 5
            else:
                height += 1

    if died:
        print(-1)
    else:
        print(height)
    


