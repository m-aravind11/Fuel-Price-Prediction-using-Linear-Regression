import csv
import matplotlib.pyplot as plt
from tkinter import *

def plot_diesel_week(days,d_prices):
    plt.bar(days,d_prices,color=(0.26,0.52,0.28,1),width=0.55)
    plt.ylim( ( min(d_prices)-0.1,max(d_prices)+0.1 ))
    plt.title('Average Diesel Price for each day of the week')
    plt.xlabel('DAY',size=13)
    plt.ylabel('Average Diesel Price (in Rs)',size=10)
    plt.show()  

def plot_petrol_week(days,p_prices):
    plt.bar(days,p_prices,color=(0.26,0.52,0.28,1),width=0.55)
    plt.ylim( ( min(p_prices)-0.1,max(p_prices)+0.1 ))
    plt.title('Average Petrol Price for each day of the week')
    plt.xlabel('DAY',size=13)
    plt.ylabel('Average Petrol Price (in Rs)',size=10)
    plt.show()  

diesel_price=[]
petrol_price=[]
barrel_price=[]
days_of_week=[]

with open('Fuel_Datasheet.csv','r') as csvfile:
    contents=csv.reader(csvfile,delimiter=',')

    for column in contents:
        diesel_price.append(column[7])
        petrol_price.append(column[6])
        barrel_price.append(column[11])
        days_of_week.append(column[5][0:3])

csvfile.close()

del diesel_price[0:3]
del petrol_price[0:3]
del barrel_price[0:3]
del days_of_week[0:3]

#Convering String to Float Values
for i in range (len(barrel_price)):
    barrel_price[i]=float(barrel_price[i])
for i in range (len(petrol_price)):
    petrol_price[i]=float(petrol_price[i])
for i in range (len(diesel_price)):
    diesel_price[i]=float(diesel_price[i])

day_petrol={}
day_diesel={}

#Adding {day:totalPrice} for both Petrol and Diesel
for i in range(len(petrol_price)):
    if days_of_week[i] not in day_petrol:
        day_petrol[days_of_week[i]]=petrol_price[i]
    else:
        day_petrol[days_of_week[i]]+=petrol_price[i]

for i in range(len(diesel_price)):
    if days_of_week[i] not in day_diesel:
        day_diesel[days_of_week[i]]=diesel_price[i]
    else:
        day_diesel[days_of_week[i]]+=diesel_price[i]

#Finding Sum of Petrol&Diesel Pries per day of the week
for key in day_petrol.keys():
    day_petrol[key]=day_petrol[key]/days_of_week.count(key)

for key in day_diesel.keys():
    day_diesel[key]=day_diesel[key]/days_of_week.count(key)

#Finding Avg of Petrol&Diesel prices per day of the week from the Sum
print ('Average Petrol Prices for each day of the week')
for item in day_petrol.items():
    print(item[0],end=' - ')
    print(round(item[1],4))

print ('\nAverage Diesel Prices for each day of the week')
for item in day_diesel.items():
    print(item[0],end=' - ')
    print(round(item[1],4))

#Tkinter UI
root=Tk()
root.title('Fuel Prices per WeekDay')
root.minsize(350,100)
root.maxsize(350,100)

plotDiesel_week_day=Button (root,text='Avg Diesel Price (Rs) for each weekday',command=lambda : plot_diesel_week(day_diesel.keys(),day_diesel.values()))
plotDiesel_week_day.grid(row=1,column=20,padx=30,pady=10)

plotPetrol_week_day=Button (root,text='Avg Petrol Price (Rs) for each weekday',command=lambda : plot_petrol_week(day_petrol.keys(),day_petrol.values()))
plotPetrol_week_day.grid(row=3,column=20,padx=30,pady=3)

root.mainloop()
