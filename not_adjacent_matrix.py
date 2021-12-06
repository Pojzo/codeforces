t = int(input())
for i in range(t):
    n = int(input())
    if n == 1:
        print(1)
        continue

    elif n == 2:
        print(-1)
        continue

    printing_odd = True
    next_odd = 1
    next_even = 2
    for i in range(n):
        for j in range(n):
            end = " "
            if j == n - 1:
                end = "\n"
        
            if next_odd > n * n:
                printing_odd = False

            if printing_odd:
                print(next_odd, end = end)
                next_odd += 2
            else:
                print(next_even, end = end)
                next_even += 2
