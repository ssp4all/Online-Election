import math

seq = [float(x) for x in input('Enter the random sequence: ').split(',')]
i = int(input('Enter the initial position: '))
m = int(input('Enter the lag: '))
alpha = float(input('Enter the critical value: '))

N = len(seq)
M = ((N-i)//m)-1
sum = 0
for k in range(i-1,N-m,m):
    sum+=(seq[k]*seq[k+m])
rho = ((1/(M+1))*sum)-0.25
sigma = math.sqrt((13*M)+7)/(12*(M+1))
z = rho/sigma

if -alpha < z < alpha:
    print("\nThe random sequence is independent")
else:
    print("\nThe random sequence is not independent")

