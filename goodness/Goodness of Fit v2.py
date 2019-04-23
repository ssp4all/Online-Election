import math

stats = {int(x):[int(y)] for x,y in zip(input("Class Intervals: ").split(','),
                                            input("Frequencies: ").split(','))}
threshold = float(input("Critical Value: "))
n = int(input("Time Period: "))

print(stats)

mean = chi = 0
for i in stats:
    mean+=i*stats[i][0]
mean = round(mean/n,2)

for i in stats:
    Pi = (math.exp(-mean)*mean**i)/math.factorial(i)
    Ei = round(n*Pi,2)
    stats[i].append(Ei)

print(stats)


Oi = Ei = 0
for i in sorted(stats.keys(), reverse=True):
    if Ei<5 or stats[i][1]<5:
        Oi+=stats[i][0]
        Ei+=stats[i][1]
        stats.pop(i)
stats[-1]=[Oi]
stats[-1].append(Ei)

for i in stats:
    chi+=(stats[i][0]-stats[i][1])**2/stats[i][1]

if round(chi,2)<threshold:
    print("\nHypothesis is accepted")
else:
    print("\nHypothesis is rejected")
