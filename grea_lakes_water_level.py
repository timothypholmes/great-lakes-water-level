#! /usr/bin/env python3

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib as mpl
#import seaborn as sns


data = pd.read_csv('~/Documents/github/great-lakes-water-level/great_lakes_mean_water_levels.csv')

d = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12 }
data['month'] = data['month'].map(d)
date = data['month'], data['year']
data["day"] = 1
data["date"] = pd.to_datetime(data[["year", "month", "day"]])
data["date"].head()
data.index = data["date"]
data = data.drop(["month", "year", "day", "date",'St. Clair'], axis=1)

#--------------------------------Year Vs. Water-level ---------------------------
colors_months = date[0] #Months
nrows = 2
ncols = 2
fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14,10))

for i in range(len(data.columns)):
    col = i % ncols
    row = i // ncols
    # Select the column at position r+c
    plot_data = data.iloc[:,i]
    # Select the axis to plot on
    ax = axes[row,col]
    img = ax.scatter(plot_data.index, plot_data.values, c=colors_months, cmap=plt.cm.winter, s=6, vmin=0, vmax=12)
    ax.title.set_text(f"Lake {plot_data.name}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Mean Water Level (Meters)")
    ax.grid(True)

fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.10, 0.02, 0.8])
cbar = fig.colorbar(img, cax=cbar_ax, ticks=[1,2,3,4,5,6,7,8,9,10,11,12])
cbar.ax.set_yticklabels(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
cbar.ax.set_title('Month')

plt.show()
fig.savefig('water_level_year.pdf')

#-------------------------------- Month Vs. Water-level ---------------------------

colors_years = date[1] #Years
nrows = 2
ncols = 2
fig, axs = plt.subplots(nrows=nrows, ncols=ncols, sharex=False, sharey=False, figsize=(14,10))

for i in range(len(data.columns)):
    col = i % ncols
    row = i // ncols
    # Select the column at position r+c
    plot_data = data.iloc[:,i]
    # Select the axis to plot on
    ax = axs[row,col]
    ax.scatter(date[0], plot_data.values, c=colors_years, cmap=plt.cm.winter, s=6)
    ax.title.set_text(f"Lake {plot_data.name}")
    ax.set_xlabel("Month")
    ax.set_ylabel("Mean Water Level (Meters)")
    ax.grid(True)

fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.10, 0.02, 0.8])
cbar = fig.colorbar(img, cax=cbar_ax, ticks=[1,2,3,4,5,6,7,8,9,10,11,12])
cbar.ax.set_yticklabels(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
cbar.ax.set_title('Month')

plt.show()
fig.savefig('water_level_year.pdf')

#-------------------------------- Month Vs. Min-Max-Water-level ---------------------------

#data = (data.resample('Y').agg(['min', 'max']))
#year = np.arange(1917,2019)
'''#plt.tight_layout()
nrows = 2
ncols = 2
fig, axs = plt.subplots(nrows=nrows, ncols=ncols, sharex=False, sharey=False)
fig.set_size_inches(10,6)
for i in range(len(data.columns)):
    col = i % ncols
    row = i // ncols
    # Select the column at position r+c
    plot_data = data.iloc[:,i]
    # Select the axis to plot on
    ax = axs[row,col]
    ax.scatter(date[0], plot_data.values, c=plot_data.values, cmap=plt.cm.cividis, s=6)
    ax.title.set_text(f"Lake {plot_data.name}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Mean Water Level (Meters)")
    ax.grid(True)
    
plt.tight_layout()
plt.show()
fig.savefig('water_level_month.pdf')
'''
#--------------------------------seaborn.heatmap---------------------------
#water_level = data.pivot("month", "year", "Michigan-Huron")
#months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

