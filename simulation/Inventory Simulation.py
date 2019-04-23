from decimal import Decimal

a,b = [int(x) for x in input("Daily Demand Range: ").split('-') if x.isdigit()]
probability = [Decimal(x) for x in input("Distribution of Probabilities: ").split(',') if 0<Decimal(x)<1]
demand_random = [int(x) for x in input("Random Digits: ").split(',') if x.isdigit()]
demand = [[a,b] for a,b in zip(range(a,b+1),probability)]
print()
a,b = [int(x) for x in input("Lead Time Range: ").split('-') if x.isdigit()]
probability = [Decimal(x) for x in input("Distribution of Probabilities: ").split(',') if 0<Decimal(x)<1]
lead_random = [int(x) for x in input("Random Digits: ").split(',') if x.isdigit()]
lead = [[a,b] for a,b in zip(range(a,b+1),probability)]
print()
initial, mx = [int(x) for x in input("Initial and Maximum Inventory levels: ").split(',') if x.isdigit()]
weeks, days = [int(x) for x in input("Number of Weeks, Days in a week: ").split(',') if x.isdigit()]
shipment, duration = [int(x) for x in input("Next Shipment Quantity, Days to Arrival: ").split(',') if x.isdigit()]  

temp, rand = 0, 1
for i in range(len(demand)):
    temp+=demand[i][1]
    demand[i].append(temp)                   
    demand[i].append([rand,int(str(demand[i][2]).split('.')[1])+1])
    rand = demand[i][3][1]
    if rand == 1:
        demand[i][3][1] = 10**len(str(demand[i][3][0]))

temp, rand = 0, 1
for i in range(len(lead)):
    temp+=lead[i][1]
    lead[i].append(temp)
    lead[i].append([rand,int(str(lead[i][2]).split('.')[1])+1])
    rand = lead[i][3][1]
    if rand == 1:
        lead[i][3][1] = 10**len(str(lead[i][3][0]))

print()
print("{0:<12}{0:<12}{1:<12}{2:<14}{0:12}{3:<12}{0:<12}{4:<12}{2:<14}{5:<14}"\
      .format(" ","Start","Random Digit","End","Shipment","Days Until"))
print("{0:<12}{1:<12}{2:<12}{3:<14}{4:<12}{2:<12}{5:<12}{6:<12}{7:<14}{8:<14}"\
      .format("Cycle","Day","Inventory","(Demand)","Demand","Shortage","Quantity","(Lead Time)","Next Shipment"))
print("="*126)

shortage = counter = average = 0
for week in range(1,weeks+1):
    print("{:<12}".format(week),end='')
    temp = duration
    for day in range(1,days+1):
        index = ((week-1)*days+day)-1
        if demand_random[index] == 0:
            order = len(demand)+shortage
        else:
            order = [x[0] for x in demand if demand_random[index] in range(*x[3])][0] + shortage
        if day == duration+1:
            initial+=shipment
        if order > initial:
            eventual = 0
            shortage = order-initial
            counter+=1
        else:
            eventual = initial-order
            shortage = 0
            average += eventual
        if day != days:
            if temp != 0:
                temp -= 1
                print("{0:<12}{1:<12}{2:<14}{3:<12}{4:<12}{5:<12}{6:12}{6:14}{7:<14}"\
                  .format(day,initial,demand_random[index],order,eventual,shortage," ",temp))
            else:
                print("{:<12}{:<12}{:<14}{:<12}{:<12}{:<12}"\
                  .format(day,initial,demand_random[index],order,eventual,shortage))
            print("{:12}".format(" "),end='')
        else:
            print("{:<12}{:<12}{:<14}{:<12}{:<12}{:<12}"\
                  .format(day,initial,demand_random[index],order,eventual,shortage),end='')
        initial = eventual
    shipment = mx-eventual
    if lead_random[week-1] == 0:
        duration = len(lead)
    else:
        duration = [x[0] for x in lead if lead_random[week-1] in range(*x[3])][0]
    print("{:<12}{:<14}{:<14}".format(shipment,lead_random[week-1],duration))
    if week != weeks: print("-"*126)
        
print("="*126)
print("Shortage:",counter,"days")
print("Average End Inventory:",average/(weeks*days))
