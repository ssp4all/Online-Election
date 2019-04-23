ip = [2, 334, 5, 4]
n = 4

dp, dm = [0]*n, [0]*n
x = [0]*n
print(x)
a, c, m = 5, 10, 15
x[0] = 0.1

for i in range(1, n):
	print(i)
	x[i] = ( ( a * x[i-1] + c) % m) / m
	print(x[i])

x.sort()

print("Sorted numbers are: ")
print(x)
dpmax, dmmax = 0, 0
for i in range(1,n):
	dp[i] = (i+1)/n - x[i]
	dm[i] = x[i] - i/n
	dpmax = max(dp[i], dpmax)
	dmmax = min(dm[i], dmmax)

d = max(dmmax, dpmax)
if d<0.565:
	print ('Uniform')
else:
	print('Non-uniform')
		
