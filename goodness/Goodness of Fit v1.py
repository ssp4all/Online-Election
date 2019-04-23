import math

classIntervals = [int(x) for x in input("Class Intervals: ").split(',')]
frequency = [int(x) for x in input("Frequencies: ").split(',')]
alpha = float(input("Critical Value: "))
n = int(input("TIme Period: "))

mean = chi = 0
for x,f in zip(classIntervals,frequency):
    mean+=(f*x)
mean = round(mean/n,2)

stats = {x:[y] for x,y in zip(classIntervals,frequency)}
for Xi in stats:
    Pi = (math.exp(-mean)*(mean**Xi))/math.factorial(Xi)
    Ei = round(n*Pi,2)
    stats[Xi].append(Ei)

Oi = Ei = 0
for i in sorted(stats.keys(),reverse=True):
    if Ei<5 or stats[i][1]<5:
        Oi+=stats[i][0]
        Ei+=stats[i][1]
        stats.pop(i)
stats[-1] = [Oi]
stats[-1].append(Ei)

for i in stats:
    chi+=(stats[i][0]-stats[i][1])**2/stats[i][1]

if round(chi,2) < alpha:
    print("\nHypothesis is accepted")
else:
    print("\nHypothesis is rejected")
