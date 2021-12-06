t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    answer = "NO"
    first = set()
    second = set()
    for i in range(n):
        if not nums[i] in first:
            first.add(nums[i])
        else:
            if nums[i] != nums[i - 1] or nums[i] in second:
                answer = "YES"
                break

            second.add(nums[i])

    print(answer)

