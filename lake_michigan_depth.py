#! /usr/bin/env python3
import numpy as np 
import pandas as pd 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#import seaborn as sns


data = pd.read_csv('~/Desktop/new_lake.csv')

#flights = sns.load_dataset("flights")

d = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12 }
data['month'] = data['month'].map(d)

#seaborn.heatmap
#water_level = data.pivot("month", "year", "Michigan-Huron")
#months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


date = data['month'], data['year']
lake_michigan_huron_depth = data['Michigan-Huron']
lake_Superior_depth = data['Superior'] 
lake_StClair_depth = data['St. Clair'] 
lake_Erie_depth = data['Erie'] 
lake_Ontario_depth = data['Ontario'] 
#print(data)



fig = plt.figure(figsize=(10,8))

ax21 = fig.add_subplot(221, projection='3d')
ax22 = fig.add_subplot(222, projection='3d')
ax23 = fig.add_subplot(223, projection='3d')
ax24 = fig.add_subplot(224, projection='3d')

x = date[0]
y = date[1]
c = lake_michigan_huron_depth

img = ax21.scatter(x, y, lake_michigan_huron_depth, c=c, cmap=plt.cm.cividis)
img = ax22.scatter(x, y, lake_Superior_depth, c=c, cmap=plt.cm.cividis)
img = ax23.scatter(x, y, lake_Erie_depth, c=c, cmap=plt.cm.cividis)
img = ax24.scatter(x, y, lake_Ontario_depth, c=c, cmap=plt.cm.cividis)
cbar_ax = fig.add_axes([0.5, 0, 0.03, 0.1])
fig.colorbar(img, orientation = "horizontal")
#winter
#coolwarm
#ocean

ax21.title.set_text('Lake Michigan-Huron')

ax21.set_xlabel('Month')
ax21.set_ylabel('Year')
ax21.set_zlabel('Depth (Meters)')
ax21.view_init(azim=0, elev=0)
#ax22.view_init(azim=90, elev=0)

ax22.title.set_text('Lake Superior')

ax22.set_xlabel('Month')
ax22.set_ylabel('Year')
ax22.set_zlabel('Depth (Meters)')
ax22.view_init(azim=0, elev=0)
#ax22.view_init(azim=90, elev=0)

ax23.title.set_text('Lake Erie')

ax23.set_xlabel('Month')
ax23.set_ylabel('Year')
ax23.set_zlabel('Depth (Meters)')
ax23.view_init(azim=0, elev=0)
#ax22.view_init(azim=90, elev=0)

ax24.title.set_text('Lake Ontario')

ax24.set_xlabel('Month')
ax24.set_ylabel('Year')
ax24.set_zlabel('Depth (Meters)')
ax24.view_init(azim=0, elev=0)
#ax22.view_init(azim=90, elev=0)


'''
#Animate
for ii in range(0,360,1):
        ax21.view_init(elev=10., azim=ii)
        savefig("movie%d.png" % ii)
'''

plt.show()

fig2 = plt.figure(figsize=(8,6))
ax = fig2.add_subplot(111)
x = range(0, len(x))
#Jan 2010 to present (May 2019)
yg = ax.plot(x[1105:1217], lake_michigan_huron_depth[1105:1217])


#plt.show()


'''
fig3 = plt.figure(figsize=(8,6))
axbar = fig3.add_subplot(111, projection='3d')
#Bar graph
x3 = date[0]
y3 = date[1]
z3 = np.zeros(len(date[0]))

dx = np.ones(len(date[0]))
dy = np.ones(len(date[0]))
dz = lake_michigan_huron_depth

axbar.set_zlim3d(min(lake_michigan_huron_depth),max(lake_michigan_huron_depth))
axbar.bar3d(x3, y3, z3, dx, dy, dz)

#plt.show()
'''

