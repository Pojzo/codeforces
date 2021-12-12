
min_distance = 9999999999999

def dfs(leftover, prev_pos, pos, k, bags, distance):
    distance += abs(prev_pos - pos)
    if not len(leftover):
        global min_distance
        min_distance = min(min_distance, distance)

    if bags == 0:
        distance += abs(pos)
        pos = 0

    for i in leftover:
        dfs([x for x in leftover if not x == i], pos, i, k, bags - 1, distance)


t = int(input())
for x in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    min_distance = 9999999999999
    dfs(list(nums), 0, 0, k, k, 0)
    print("OUTPUT", min_distance)

    
