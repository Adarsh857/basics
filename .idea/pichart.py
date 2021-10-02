import matplotlib.pyplot as plt
labels=['pulao','biryani','paneer','palak']
sizes=[10,20,30,40]
explode=(0,0.1,0,0)
fig1,ax1=plt.subplots()
#ax1.pie(sizes,labels=labels)
ax1.pie(sizes, explode=explode,labels=labels)
ax1.axis('equal')
plt.show()