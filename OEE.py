import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_and_plot(month):
    file_path = f'D:\\OEE\\{month}.csv'
    data = pd.read_csv(month +".csv")
    value = data.tail(1).values[0]
    plt.figure(figsize=(10, 5))
    plt.bar(info, value, color=col, width=0.5)
    plt.ylim(70, 100)
    plt.ylabel('in Percentage')
    plt.title(f'Records of {month}')
    plt.show()
    return value

print('''So OEE is a framework of measuring the efficiency and effectiveness of a process, 
      by breaking it down into three constituent components (Availability, Productivity, Quality). 
      OEE helps you identify and measure problems so you can fix it, and it also provides a 
      standardized method of benchmarking process.''')

print('Now lets look at factors on which OEE depends')
print('The major 3 factors are\n 1. Availability\n 2. Performance\n 3. Quality')

print("Now let's have a look at their formulas\n\n")
print('Availability = Run Time / Planned Production Time \n\n')
print('Performance = (Ideal Cycle Time × Total Count) / Run Time \n\n')
print('Quality = Good Count / Total Count \n\n')
print('OEE = Availability X Performance X Quality')
print()
print('So for this project our product is:- Gear hobbing machine')
print('Lets compare its OEE for 4 months')

#Variables used
info=['Availability','Performance','Quality','Total OEE']
col=['Red','Blue','Orange','Green']

#Ploting
A=read_and_plot("April")
print()
M = read_and_plot("May")
print()
JN = read_and_plot("June")
print()
JL = read_and_plot("July")
print('We can see the diversity in losses for the above months')
print('By looking at the graph we can know about the reasons for the losses in the following months and that is the main idea of OEE')

print("Okay, now let's have a look at the final comparison of OEE of all the months\n")
print() 
df1=pd.DataFrame([A,M,JN,JL],index=['April','May','June','July'], columns=info)
x=df1['Total OEE']
y=df1.index
l1=x.values.tolist()
l2=y.values.tolist()
l3=[85]*4
plt.figure(figsize=(14,7))
plt.ylim(80,90)
plt.plot(l2,l1,linewidth=4,marker='o',markersize=8,markeredgecolor = 'Red',label='Actual OEE')
plt.plot(l3,linewidth=2,linestyle='dashed',label='Ideal OEE')
plt.title('Comparison of all months')
plt.legend()
plt.show()

print('Here we can see that the values of OEE are below the ideal value, i.e, 85%')

print('But it also shows us the improvement which is due to the rectifications of the error which we can know by comparing the graphs and having a look at the area which causes the maximum losses')

print('Lets try calculating our OEE performance')
print('----'*20)
RT=float(input('Enter the run time (in min) :'))
PPT=float(input('Enter the planned production time (in min) :'))
ICT=float(input('Enter the ideal cycle time (in min) :'))
TC=float(input('Enter the total count of the product :'))
GC=float(input('Enter the good count of product :'))
Ava=RT/PPT
Per=(ICT*TC)/RT
Qua=GC/TC
OEE=Ava*Per*Qua
d1={'Availability %':Ava*100,'Performance %':Per*100,'Quality %':Qua*100,'OEE %':OEE*100}
Df=pd.DataFrame(d1,index=[1])
print('----'*20)
print(Df)
Df.to_csv('D:\\OEE\\NewValues.csv',index=False)
