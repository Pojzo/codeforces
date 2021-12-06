t = int(input())
for i in range(t):
    string = input()
    # count consecutive Ls
    max_ls = max_current = 0
    for x in range(len(string)):
        if string[x] == 'L':
            max_current += 1
        else:
            max_ls = max(max_ls, max_current)
            max_current = 0

    max_ls = max(max_ls, max_current)

    print(max_ls + 1)
