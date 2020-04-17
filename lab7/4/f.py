n = int(input())
num = [int(i) for i in input().split()]
cnt = 0
for x in range(1,n-1):
	if num[x] > num[x-1] and num[x] > num[x+1]:
		cnt = cnt + 1

print(cnt)