t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    pos = n - 1
    while pos > 0 and nums[pos - 1] >= nums[pos]:
        pos -= 1

    while pos > 0 and nums[pos - 1] <=  nums[pos]:
        pos -= 1
    
    print(pos)
