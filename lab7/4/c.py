n = int(input())
cnt = 0
num = [int(i) for i in input().split()]
for x in range(n):
	if num[x]>0:
		cnt = cnt + 1

print(cnt)