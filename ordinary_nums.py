t = int(input())
for i in range(t):
    n = int(input())
    i = 0
    count = 0
    while n != 0:
        count += (n % 10) * 10 ** i 
        n //= 10
        i += 1
 
    print(count)
