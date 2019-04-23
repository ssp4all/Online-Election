seq = [[float(x)] for x in input("Enter the random sequece: ").split(',') if 0<=float(x)<1]
alpha = float(input("Enter the critical value: "))
seq.sort()                                      #seq[i][0]: R(i) 
N = len(seq)

for i in range(N):
    seq[i].append((i+1)/N)                      #seq[i][1]: i/N
    seq[i].append(seq[i][1]-seq[i][0])          #seq[i][2]: i/N - R(i)
    seq[i].append(seq[i][0]-i/N)                #seq[i][3]: R(i) - (i-1)/N

Dplus = max([s[2] for s in seq if s[2]>=0])
Dminus = max([s[3] for s in seq if s[3]>=0])
D = max(Dplus, Dminus)

if D < alpha:
    print("\nThe random sequence is uniformly distributed")
else:
    print("\nThe random sequence is not uniformly distributed")