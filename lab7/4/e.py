n = int(input())
num = [int(i) for i in input().split()]

for x in range(0,n):
	if x == n-1:
		print("NO")
	elif num[x] > 0 and num[x+1] > 0:
		print("YES")
		break
	elif num[x] < 0 and num[x+1] < 0:
		print("YES")
		break
