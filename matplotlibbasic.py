import matplotlib.pyplot as plt
months = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','sep','Oct','Nov','Dec']
sales = [45,52,48,61,58,72,69,75,68,82,90,95]

plt.figure(figsize=(12,5))
plt.plot(months,sales,marker='o',color='red',linewidth=2,markersize = 8)
plt.fill_between(months,sales,alpha =0.15,color = 'steelblue')
plt.title('Montlhy Sales 2024 (Rs . thoushand)',fontsize = 14)
plt.xlabel('Months')
plt.ylabel('Sales  ')
plt.grid(True, alpha = 0.3)
plt.tight_layout()
plt.show()

cities =['Bhopal','Indore','Jabalpu','Gwalior','Ujjain']
students = [1200,2800,980,850,650]
colors = ['#2196f3','#4CAF50','#ff9800','#9C27B0','#f44336']

plt.figure(figsize=(9,5)) 
bars = plt.bar(cities,students ,color=colors,edgecolor  = 'white',linewidth = 1.5)
plt.title('student enroll per city')
plt.ylabel('Number pf student')

for bar,val in zip(bars,students):
    plt.text(bar.get_x()+bar.get_width()/2,val+30, str(val), ha = 'center',fontweight = 'bold')
plt.tight_layout()
plt.show()    


import numpy as np 
study_hrs = np.random.uniform(2,10,50)
marks  = study_hrs * 7 +np.random.normal(0,8,50)
marks = np.clip(marks,30 ,100)

plt.figure(figsize=(8,5))
plt.scatter(study_hrs,marks,c=marks,cmap='RdYlGn',s =100,alpha = 0.8)
plt.colorbar(label ='Marks')
plt.title('study Hours vs Exam')
plt.xlabel('Study Hours\Day')
plt.ylabel('Exam Marks')
plt.tight_layout()
plt.show()