'''
    Time and Space Efficient!
        v1 runtime : 90.90ms (sample size = 40)
        v2 runtime : 04.96ms (sample size = 40)
'''

n = 10
N = chi = interval = 0
step = (0.0+1.0)/n

count = {}
for i in range(n):
    interval += step
    count[round(interval,2)] = 0

for x in sorted(input('Enter the random sequence: ').split(',')):
    N += 1
    for k in sorted(count.keys()):
        if float(x) < k:
            count[k] = count[k]+1
            break

alpha = float(input("Enter the critical value: "))

Ei = N/n
for k in count:
    chi+=(count[k]-Ei)**2/Ei

if round(chi,2) < alpha:
    print("\nThe random sequence is uniformly distributed")
else:
    print("\nThe random sequence is not uniformly distributed")
