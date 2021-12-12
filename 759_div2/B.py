t = int(input())
for x in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    if len(set(nums)) == 1:
        print(0)
        continue
 
    x = nums[n - 1]
    k = 0
    max_num = 0
    max_index = 0
    for index, num in enumerate(nums):
        if num >= max_num:
            max_num = num
            max_index = index
    
    if max_index == n - 1:
        print(0)
        continue
    second_max_index = 0
    second_max = 0
    for i in range(max_index + 1, len(nums)):
        if nums[i] >= second_max and nums[i] != max_num:
            second_max = nums[i]
            second_max_index = i

    print(len(nums) - second_max_index)
