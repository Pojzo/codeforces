def f(x, cur):
    i = len(x) - 1

    remove = 0
    while i >= 0 and x[i] != cur[1]:
        remove += 1
        i -= 1

    if i < 0:
        return 999999

    i -= 1

    while i >= 0 and x[i] != cur[0]:
        i -= 1
        remove += 1

    if i < 0:
        return 999999
    
    return remove



n = int(input())
for i in range(n):
    x = input()
    s = ["25", "50", "75", "00"]
    min_remove = 9999
    for string in s:
        min_remove = min(min_remove, f(x, string))

    print(min_remove)

