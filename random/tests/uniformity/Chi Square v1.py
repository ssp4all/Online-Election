seq = [float(x) for x in input("Enter the random sequece: ").split(',') if 0<=float(x)<1]
alpha = float(input("Enter the critical value: "))

n = 10
N = len(seq)
Ei = N/n
step = (0.0+1.0)/n

interval = chi = 0
for i in range(n):
    count = 0
    for x in seq:
        if round(interval,2) <= x < round(interval+step,2):
            count+=1
    chi+=(count-Ei)**2/Ei
    interval+=step

if chi < alpha:
    print("\nThe random sequence is uniformly distributed")
else:
    print("\nThe random sequence is not uniformly distributed")
