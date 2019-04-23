import re, math

runs = [float(x) for x in input("Enter the random sequece: ").split(',') if 0<=float(x)<1]
alpha = float(input("Enter the critical value: "))

N = len(runs)
for i in range(N-1):
    runs[i] = '+' if runs[i]<runs[i+1] else '-'
runs = ''.join(runs[:N-1])
runs = re.findall(r'\++|-+',runs)
a = len(runs)
mean = (2*N-1)/3
variance = (16*N-29)/90
z = (a-mean)/math.sqrt(variance)

if -alpha < z < alpha:
    print("\nThe random sequence is independent")
else:
    print("\nThe random sequence is not independent")
