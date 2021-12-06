n = int(input())
teacher = list(map(int, input().split()))
students = list(map(int, input().split()))


result = [x - y for x, y in zip(teacher, students)]
result.sort()

count = 0
right = n - 1
left = 0

while left < right:
    if result[right] + result[left] > 0:
        count += right - left
        right -= 1
    else:
        left += 1

print(count)
