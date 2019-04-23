import re, math

runs = [float(x) for x in input("Enter the random sequece: ").split(',') if 0<=float(x)<1]
alpha = float(input("Enter the critical value: "))
mn, mx = [float(x) for x in input("Enter range of random sequence: ").split('-') if 0<=float(x)<1]

N = len(runs)
mean = (mn+mx)/2
for i in range(N):
    runs[i] = '-' if runs[i]<mean else '+'
runs = ''.join(runs)
n1 = runs.count('+')
n2 = runs.count('-')
runs = re.findall(r'\++|-+',runs)
b = len(runs)
mean = ((2*n1*n2)/N)+0.5
variance = (2*n1*n2*(2*n1*n2-N))/(N**2*(N-1))
z = (b-mean)/math.sqrt(variance)

if -alpha < z < alpha:
    print("\nThe random sequence is independent")
else:
    print("\nThe random sequence is not independent")
