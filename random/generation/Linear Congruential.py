x0 = float(input('Enter the seed: '))
a = float(input('Enter the multiplier: '))
c = float(input('Enter the increment: '))
m = float(input('Enter the modulus: '))
n = int(input('Enter the number of random numbers to generate: '))

xi = x0 ; p = 0
print('Random Numbers:',end=' ')
for i in range(n):
    xi = ((a*xi)+c)%m
    ri = xi/m
    print('%.4f'%ri,end=' ')
    if xi == x0 and not p:
        p = i+1

if not p:
    p = i+1
    while xi != x0:
        xi = ((a*xi)+c)%m
        p += 1

print('\nPeriod:',p)

    
