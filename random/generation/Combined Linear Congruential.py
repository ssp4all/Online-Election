data = []
x0,a,c,m = range(4)
k = int(input('Enter the number of generators: '))
p = 1
for i in range(k):
    data.append([])
    print('Data for Generator',i+1,' :')
    data[i].append(float(input('\tEnter the seed: ')))          # x0
    data[i].append(float(input('\tEnter the multiplier: ')))    # a
    data[i].append(float(input('\tEnter the increment: ')))     # c
    data[i].append(float(input('\tEnter the modulus: ')))       # m
    p *= data[i][m]-1
n = int(input('Enter the number of random numbers to generate: '))
p /= 2**(k-1)
print('Random Numbers:',end=' ')
for j in range(n):
    x = 0
    for i in range(k):
        data[i][x0] = ((data[i][a]*data[i][x0])+data[i][c])%data[i][m]
        x += ((-1)**i)*data[i][x0]
    x = x%(data[i][m]-1)
    ri = x/data[j][m] if x>0 else (data[j][m]-1)/data[j][m]
    print('%.4f'%ri,end=' ')
print('\nMaximum possible Period:',p)
