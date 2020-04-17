n = int(input())
num = [int(i) for i in input().split()]
for x in range(0,n):
	if num[x]%2==0:
		print(num[x])