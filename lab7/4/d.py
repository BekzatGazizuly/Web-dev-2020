n = int(input())
cnt = 0
num = [int(i) for i in input().split()]
for x in range(1,n):
	if num[x] > num [x-1]:
		cnt = cnt + 1

print(cnt)