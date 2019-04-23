from decimal import Decimal

a,b = [int(x) for x in input("Interarrival Time Range: ").split('-') if x.isdigit()]
probability = [Decimal(x) for x in input("Distribution of Probabilities: ").split(',') if 0<Decimal(x)<1]
interarrival_random = [int(x) for x in input("Random Digits: ").split(',') if x.isdigit() or x=='-1']
interarrival = [[a,b] for a,b in zip(range(a,b+1),probability)]
print()
a,b = [int(x) for x in input("Service Time Range: ").split('-') if x.isdigit()]
probability = [Decimal(x) for x in input("Distribution of Probabilities: ").split(',') if 0<Decimal(x)<1]
service_random = [int(x) for x in input("Random Digits: ").split(',') if x.isdigit()]
service = [[a,b] for a,b in zip(range(a,b+1),probability)]

temp, rand = 0, 1
for i in range(len(interarrival)):
    temp+=interarrival[i][1]
    interarrival[i].append(temp)                   
    interarrival[i].append([rand,int(str(interarrival[i][2]).split('.')[1])+1])
    rand = interarrival[i][3][1]
    if rand == 1:
        interarrival[i][3][1] = 10**len(str(interarrival[i][3][0]))
        #interarrival[i][3][1] = 10**str(interarrival[0][1])[::-1].find('.')

temp, rand = 0, 1
for i in range(len(service)):
    temp+=service[i][1]
    service[i].append(temp)
    service[i].append([rand,int(str(service[i][2]).split('.')[1])+1])
    rand = service[i][3][1]
    if rand == 1:
        service[i][3][1] = 10**len(str(service[i][3][0]))
        #service[i][3][1] = 10**str(service[0][1])[::-1].find('.')

print()
print("{1:<12}{2:12}{0:12}{1:<12}{0:12}{3:<12}{4:<12}{3:<12}{5:<12}{6:<12}"\
      .format(" ","Random","Inter-","Service","Customer","System","Total"))
print("{0:<12}{1:<12}{1:<12}{0:<12}{2:<12}{3:<12}{4:<12}{5:<12}{6:<12}{7:<12}"\
      .format("Digit","Arrival","Service","Begin","Wait","End","Idle","Time in"))
print("{1:<12}{0:<12}{0:<12}{2:<12}{0:<12}{0:<12}{0:<12}{0:<12}{0:<12}{3:<12}"\
      .format("Time","(Arrival)","(Service)","System"))
print("="*120)

customers = [[a,b] for a,b in zip(interarrival_random,service_random)]
#customers[i][0]: Random Digit (Interarrival), customers[i][1]: Random Digit (Service)
n = len(customers)
prev = pre = 0
for i in range(n):
    if customers[i][0] is -1:
        customers[i].append(0)                              #customers[i][2]: Interarrival Time
    elif customers[i][0] is 0:
        customers[i].append(len(interarrival))              #customers[i][2]: Interarrival Time
    else:
        temp = [x[0] for x in interarrival if customers[i][0] in range(*x[3])]
        customers[i].append(temp[0])                        #customers[i][2]: Interarrival Time
    customers[i].append(pre+customers[i][2])                #customers[i][3]: Arrival Time
    pre = customers[i][3]
    if customers[i][1] is 0:
        customers[i].append(len(service))                   #customers[i][4]: Service Time
    else:
        temp = [x[0] for x in service if customers[i][1] in range(*x[3])]
        customers[i].append(temp[0])                        #customers[i][4]: Service Time
    if prev > customers[i][3]:
        customers[i].append(prev)                           #customers[i][5]: Service Begin Time
        customers[i].append(prev-customers[i][3])           #customers[i][6]: Waiting Time
        customers[i].append(0)                              #customers[i][7]: System Idle Time
    else:
        customers[i].append(customers[i][3])                #customers[i][5]: Service Begin Time
        customers[i].append(0)                              #customers[i][6]: Waiting Time
        customers[i].append(customers[i][3]-prev)           #customers[i][7]: System Idle Time
    customers[i].append(customers[i][5]+customers[i][4])    #customers[i][8]: Service End Time
    customers[i].append(customers[i][4]+customers[i][6])    #customers[i][9]: Total Time in the System
    prev = customers[i][8]

    print("{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}"\
          .format(customers[i][0],customers[i][2],customers[i][3],
                  customers[i][1],customers[i][4],customers[i][5],
                  customers[i][8],customers[i][6],customers[i][7],
                  customers[i][9]))

print("="*120)
print("Average Service Time: ",sum([c[4] for c in customers])/n)
print("Average Waiting Time: ",sum([c[6] for c in customers])/n)
print("Average Sytem Idle Time: ",sum([c[7] for c in customers])/n)
