import re

runs = [float(x) for x in input("Enter the random sequece: ").split(',') if 0<=float(x)<1]
alpha = float(input("Enter the critical value: "))

N = len(runs)
mean = (0.0+0.99)/2

for i in range(N):
    runs[i] = '-' if runs[i]<mean else '+'
runs = ''.join(runs)
n1 = runs.count('+')
n2 = runs.count('-')
runs = re.findall(r'\++|-+',runs)
runs = [len(x) for x in runs]

EI = (n1/n2)+(n2/n1)
EA = N/EI
stats = {}                      #key: Run Length (i)
for run in runs:
    if run not in stats:
        stats[run] = [1]        #value[0]: Observed no. of Runs (Oi)        
    else:
        stats[run][0]+=1        #value[0]: Observed no. of Runs (Oi)
sum = chi = 0
for i in stats:
    Wi = round(((n1/N)**i*(n2/N))+((n1/N)*(n2/N)**i),2)
    EYi = round((N*Wi)/EI,2)
    stats[i].append(EYi)        #value[1]: Expected no. of Runs (EYi)
    sum+=EYi
Oi, EYi = 0, round(EA-sum,2)
for i in sorted(stats.keys(),reverse=True):
    if EYi<5 or stats[i][1]<5:
        Oi+=stats[i][0]
        EYi+=stats[i][1]
        stats.pop(i)
stats[0] = [Oi]
stats[0].append(EYi)

for i in stats:
    chi+=(stats[i][0]-stats[i][1])**2/stats[i][1]

if round(chi,2) < alpha:
    print("\nThe random sequence is independent")
else:
    print("\nThe random sequence is not independent")
