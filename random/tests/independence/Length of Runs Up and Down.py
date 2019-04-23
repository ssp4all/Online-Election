import re, math

runs = [float(x) for x in input("Enter the random sequece: ").split(',') if 0<=float(x)<1]
alpha = float(input("Enter the critical value: "))

N = len(runs)
mean = (2*N-1)/3

for i in range(N-1):
    runs[i] = '+' if runs[i]<runs[i+1] else '-'
runs = ''.join(runs[:N-1])
runs = re.findall(r'\++|-+',runs)
runs = [len(x) for x in runs]

stats = {}                      #key: Run Length (i)
for run in runs:
    if run not in stats:
        stats[run] = [1]        #value[0]: Observed no. of Runs (Oi)        
    else:
        stats[run][0]+=1        #value[0]: Observed no. of Runs (Oi)
sum = chi = 0
for i in stats:
    if i<=N-2:
        EYi = round(2/math.factorial(i+3)*(N*(i**2+3*i+1)-(i**3+3*i**2-i-4)),2)
    elif i==N-1:
        EYi = round(2/math.factorial(N),2)
    stats[i].append(EYi)        #value[1]: Expected no. of Runs (EYi)
    sum+=EYi
Oi, EYi = 0, round(mean-sum,2)
for i in sorted(stats.keys(),reverse=True):
    if EYi<5 or stats[i][1]<5:
        Oi+=stats[i][0]
        EYi+=stats[i][1]
        stats.pop(i)
stats[0] = [Oi]
stats[0].append(EYi)
print(stats)
for i in stats:
    chi+=(stats[i][0]-stats[i][1])**2/stats[i][1]

if round(chi,2) < alpha:
    print("\nThe random sequence is independent")
else:
    print("\nThe random sequence is not independent")
