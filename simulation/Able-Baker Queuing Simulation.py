from decimal import Decimal

def service(i,beg,arr,able=True):    
    if able:
        temp = [x[0] for x in able_service if customers[i][1] in range(*x[3])][0] if customers[i][1] is not 0 else len(able_service)            
        customers[i].append(temp)                           #customers[i][4] : Service Duration (Able)
        customers[i].append(beg)                            #customers[i][5] : Service Begin (Able)
        customers[i].append(temp+beg)                       #customers[i][6] : Service End (Able)
        customers[i].append(0)                              #customers[i][7] : Service Duration (Baker)
        customers[i].append(0)                              #customers[i][8] : Service Begin (Baker)
        customers[i].append(0)                              #customers[i][9] : Service End (Baker)
        customers[i].append(beg-arr)                        #customers[i][10]: Waiting Time
    else:
        customers[i].append(0)                              #customers[i][4] : Service Duration (Able)
        customers[i].append(0)                              #customers[i][5] : Service Begin (Able)
        customers[i].append(0)                              #customers[i][6] : Service End (Able)
        temp = [x[0] for x in baker_service if customers[i][1] in range(*x[3])][0] if customers[i][1] is not 0 else len(baker_service)            
        customers[i].append(temp)                           #customers[i][7] : Service Duration (Baker)
        customers[i].append(beg)                            #customers[i][8] : Service Begin (Baker)
        customers[i].append(temp+beg)                       #customers[i][9] : Service End (Baker)
        customers[i].append(beg-arr)                        #customers[i][10]: Waiting Time

a,b = [int(x) for x in input("Interarrival Time Range: ").split('-') if x.isdigit()]
probability = [Decimal(x) for x in input("Distribution of Probabilities: ").split(',') if 0<Decimal(x)<1]
interarrival_random = [int(x) for x in input("Random Digits: ").split(',') if x.isdigit() or x=='-1']
interarrival = [[a,b] for a,b in zip(range(a,b+1),probability)]
print()
a,b = [int(x) for x in input("Service Time Range (Able): ").split('-') if x.isdigit()]
probability = [Decimal(x) for x in input("Distribution of Probabilities: ").split(',') if 0<Decimal(x)<1]
able_service = [[a,b] for a,b in zip(range(a,b+1),probability)]
print()
a,b = [int(x) for x in input("Service Time Range (Baker): ").split('-') if x.isdigit()]
probability = [Decimal(x) for x in input("Distribution of Probabilities: ").split(',') if 0<Decimal(x)<1]
baker_service = [[a,b] for a,b in zip(range(a,b+1),probability)]
print()
service_random = [int(x) for x in input("Random Digits for Service: ").split(',') if x.isdigit()]

temp, rand = 0, 1
for i in range(len(interarrival)):
    temp+=interarrival[i][1]
    interarrival[i].append(temp)
    interarrival[i].append([rand,int(str(interarrival[i][2]).split('.')[1])+1])
    rand = interarrival[i][3][1]
    if rand == 1:
        interarrival[i][3][1] = 10**len(str(interarrival[i][3][0]))

temp, rand = 0, 1
for i in range(len(able_service)):
    temp+=able_service[i][1]
    able_service[i].append(temp)
    able_service[i].append([rand,int(str(able_service[i][2]).split('.')[1])+1])
    rand = able_service[i][3][1]
    if rand == 1:
        able_service[i][3][1] = 10**len(str(able_service[i][3][0]))

temp, rand = 0, 1
for i in range(len(baker_service)):
    temp+=baker_service[i][1]
    baker_service[i].append(temp)
    baker_service[i].append([rand,int(str(baker_service[i][2]).split('.')[1])+1])
    rand = baker_service[i][3][1]
    if rand == 1:
        baker_service[i][3][1] = 10**len(str(baker_service[i][3][0]))

print()
print("{1:<12}{2:12}{0:12}{1:<12}{3:-^34}{0}{4:-^34}{0}{0:7}"\
      .format(" ","Random","Inter-","ABLE","BAKER"))
print("{0:<12}{1:<12}{1:<12}{0:<12}{2:<12}{2:<12}{2:<12}{2:<12}{2:<12}{2:<12}{3:<7}"\
      .format("Digit","Arrival","Service","Wait"))
print("{1:<12}{0:<12}{0:<12}{2:<12}{3:<12}{4:<12}{5:<12}{3:<12}{4:<12}{5:<12}{0:<7}"\
      .format("Time","(Arrival)","(Service)","Duration","Begin","End"))
print("="*127)

customers = [[a,b] for a,b in zip(interarrival_random,service_random)]
#customers[i][0] : Random Digit (Interarrival), customers[i][1] : Random Digit (Service)
n = len(customers)
arr = able = baker = 0
for i in range(n):
    if customers[i][0] is -1:
        customers[i].append(0)                              #customers[i][2] : Interarrival Time
    elif customers[i][0] is 0:
        customers[i].append(len(interarrival))              #customers[i][2] : Interarrival Time
    else:
        temp = [x[0] for x in interarrival if customers[i][0] in range(*x[3])]
        customers[i].append(temp[0])                        #customers[i][2] : Interarrival Time
    customers[i].append(arr+customers[i][2])                #customers[i][3] : Arrival Time
    arr = customers[i][3]
    if able <= arr:
        service(i,arr,arr)
        able = customers[i][6]
    elif baker <= arr:
        service(i,arr,arr,able=False)
        baker = customers[i][9]
    else:
        if able <= baker:
            service(i,able,arr)
            able = customers[i][6]
        else:
            service(i,baker,arr,able=False)
            baker = customers[i][9]
    print("{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}{:<7}"\
          .format(customers[i][0],customers[i][2],customers[i][3],
                  customers[i][1],customers[i][4],customers[i][5],
                  customers[i][6],customers[i][7],customers[i][8],
                  customers[i][9],customers[i][10]))

print("="*127)
m = max(customers[n-1][6],customers[n-1][9])
temp = sum([c[4] for c in customers])
print("Busy Time (Able): {:.2f}% ({} minutes)".format(temp/m*100,temp))
temp = sum([c[7] for c in customers])
print("Busy Time (Baker): {:.2f}% ({} minutes)".format(temp/m*100,temp))
print("Average Waiting Time: ",sum([c[10] for c in customers])/n)
