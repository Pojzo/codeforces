t = int(input())
for i in range(t):
    n = int(input())
    if n % 2 == 0:
        print(0)
        continue
    n = str(n)
    if int(n[0]) % 2 == 0:
        print(1)
        continue

    found = False
    for letter in n:
        if int(letter) % 2 == 0:
            found = True
            break
    if found:
        print(2)
    else:
        print(-1)



