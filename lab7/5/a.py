def my_min(a,b,c,d):
	e = min(a,b)
	f = min(c,d)
	ans = min(e,f)
	print(ans)


num = [int(i) for i in input().split()]
my_min(num[0],num[1],num[2],num[3])