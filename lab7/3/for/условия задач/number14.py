n = int(input())
cur = 1
cnt = 0
for i in range(0, n):
    print(cur)
    cnt += 1
    if cur == cnt:
        cur += 1
        cnt = 0
