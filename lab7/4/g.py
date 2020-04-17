n = int(input())
num = [int(i) for i in input().split()]
for x in range(int(n/2)):
	a = num[x]
	num[x] = num[n - x - 1]
	num[n - x - 1] = a

for x in range(n):
	print(num[x])