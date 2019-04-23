data = [int(x) for x in input('Enter the sequence of digits: ').split(',')]
alpha = float(input('Enter the critical value: '))

temp = {}
gaps = []
for pos,digit in enumerate(data,start=1):
    prev = temp.get(digit,None)
    temp[digit] = pos
    if prev:
        gaps.append(pos-prev-1)

N = len(data)-len(temp)
m = max(gaps)
step = round(m/10)
data = []
for i in range(0,m+1,step):
    data.append([(i,i+4)])                          # data[i][0]: range
Snx = 0; D = 0
for i in range(len(data)):
    fr = 0                                          # frequency
    for j in range(data[i][0][0],data[i][0][1]):
        fr+=gaps.count(j)
    rel = fr/N                                      # relative frequency
    Snx += rel                                      # cumulative
    Fx = 1-(0.9**data[i][0][1])                     # CDF
    d = abs(Fx-Snx)
    if d > D:
        D = d
print(D)
if D < alpha:
    print("\nThe random sequence is independent")
else:
    print("\nThe random sequence is not independent")
