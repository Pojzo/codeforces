t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    mice = list(map(int, input().split()))
    mice.sort()
    mice = [n - m for m in mice]
    seconds = 0
    end_index = k - 1
    start_index = 0
    saved = 0
    while start_index <= end_index:
        if seconds < mice[start_index]:
            saved += 1
            seconds += mice[end_index]
            end_index -= 1
            start_index += 1
        else:
            end_index -= 1

    
    if saved == 0:
        print(1)
    else:
        print(saved)
