import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore
name=input('Enter your name:')
print(Fore.BLUE,'Hello',name,'!')
print('----'*20)
print('Do you know about OEE?')
print('Menu:')
print('Yes')
print('No')
x=input('Enter your choice:')
print('----'*20)
print(Fore.MAGENTA)
if x=='Yes':
 print('That’s great, as you are already aware that by measuring OEE and the underlying losses, you will gain important insights on how to systematically improve your manufacturing process. OEE is the single best metric for identifying losses, benchmarking progress, and improving the productivity of manufacturing equipment.')
elif x=='No':
 print('It’s okay let me explain it to you')
 print('So OEE is a framework of measuring the efficiency and effectiveness of a process, by breaking it down into three constituent components (Availability, Productivity, Quality). OEE helps you identify and measure problems so you can fix it, and it also provides a standardized method of benchmarking process.')
print(Fore.RED) 
print('Now lets look at factors on which OEE depends')
print('The major 3 factors are\n 1. Availability\n 2. Performance\n 3. Quality')
print(Fore.BLUE)
print("Now let's have a look at their formulas")
print()
print(' Operating Time\n Availability = -------------------\n Planned Production Time ')
print(' \n ')
print(' Ideal Cycle Time × Total Count\n Performance = -------------------------------\n Operating Time')
print(' \n ')
print(' Good Count\nQuality = -----------\n Total Count')
print(' \n ')
print('OEE = Availability X Performance X Quality')
print()
print('So for this project our product is:- Gear hobbing machine')
print("Lets compare its OEE for 4 months")

#Variables used
info=['Availability','Performance','Quality','Total OEE']
col=['Red','Blue','Orange','Green']

#Importing the files
# April
A1=pd.read_csv('D:\\IP\\IP Project\\April month.csv')
Apr=pd.DataFrame(A1)
#print(Apr)
a=Apr.iloc[30:,7:].T
A=a[30].values
plt.figure(figsize =(10,5))
plt.bar(info,A,color=col,width=0.5)
plt.ylim(70,100)
plt.ylabel('in Percentage')
plt.title('Records of April')
plt.show()
print(Fore.RED)
print('Here the maximum loss is in Performance')

#May
M1=pd.read_csv('D:\\IP\\IP Project\\May month.csv')
May=pd.DataFrame(M1)
#print(May)
m=May.iloc[31:,7:].T
M=m[31].values

#June
J1=pd.read_csv('D:\\IP\\IP Project\\June month.csv')
June=pd.DataFrame(J1)
#print(June)
Jun=June.iloc[30:,7:].T
JUN=Jun[30].values

#July
Jl=pd.read_csv('D:\\IP\\IP Project\\July month.csv')
July=pd.DataFrame(Jl)
#print(July)
Jul=July.iloc[31:,7:].T
JL=Jul[31].values
print(Fore.MAGENTA)
print('Do you want to know about other records too?')
print('For yes enter "Yes"')
print('For no enter "No"')
x=input('Enter your option:')
print('----'*20)
if x=='Yes':
 plt.figure(figsize=(10,5))
 plt.bar(info,M,color=col,width=0.5)
 plt.ylim(70,100)
 plt.ylabel('in Percentage')
 plt.title('Records of May')
 plt.show()
 print()
 
 plt.figure(figsize=(10,5))
 plt.bar(info,JUN,color=col,width=0.5)
 plt.ylim(70,100)
 plt.title('Records of June')
 plt.ylabel('in Percentage')
 plt.show()
 print()
 
 plt.figure(figsize=(10,5))
 plt.bar(info,JL,color=col,width=0.5)
 plt.ylim(70,100)
 plt.ylabel('in Percentage')
 plt.title('Records of July')
 plt.show()
 print(Fore.MAGENTA)
 print('We can see the diversity in losses for the above months')
 print('By looking at the graph we can know about the reasons for the losses in the following months and that is the main idea of OEE')

print("Okay, now let's have a look at the final comparison of OEE of all the months")
print() 
df1=pd.DataFrame([A,M,JUN,JL],index=['April','May','June','July'], columns=info)
x=df1['Total OEE']
y=df1.index
l1=x.values.tolist()
l2=y.values.tolist()
l3=[85]*4
plt.figure(figsize=(14,7))
plt.ylim(80,90)
plt.plot(l2,l1,linewidth=4,marker='o',markersize=8,markeredgecolor = 'Red',label='Actual OEE')
plt.plot(l3,linewidth=5,linestyle='dashed',label='Ideal OEE')
plt.title('Comparison of all months')
plt.legend()
plt.show()
print(Fore.BLUE)
print('Here we can see that the values of OEE are below the ideal value, i.e, 85%')

print('But it also shows us the improvement which is due to the rectifications of the error which we can know by comparing the graphs and having a look at the area which causes the maximum losses')
print(Fore.RED)
print('Lets try calculating our OEE performance')
print('----'*20)
OT=float(input('Enter the operating time (in min) :'))
PPT=float(input('Enter the plan production time (in min) :'))
TC=float(input('Enter the total count of the product :'))
ICT=float(input('Enter the ideal cycle time (in min) :'))
GC=float(input('Enter the good count of product :'))
Ava=OT/PPT
Per=(ICT*TC)/OT
Qua=GC/TC
OEE=Ava*Per*Qua
d1={'Availability %':Ava*100,'Performance %':Per*100,'Quality %':Qua*100,'OEE %':OEE*100}
Df=pd.DataFrame(d1,index=[1])
print('----'*20)
print(Df)
Df.to_csv('D:\\IP\\IP Project\\New values.csv',index=False)

#by Shreya Rai