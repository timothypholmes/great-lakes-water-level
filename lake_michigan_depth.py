#! /usr/bin/env python3
import numpy as np 
import pandas as pd 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from os import path
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
    ax.scatter(plot_data.index, plot_data.values, c=plot_data.values, cmap=plt.cm.cividis, s=6)
    ax.title.set_text(f"Lake {plot_data.name}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Mean Water Level (Meters)")
    ax.grid(True)
    
plt.tight_layout()
plt.show()

#-------------------------------- Month Vs. Water-level ---------------------------

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
    ax.scatter(plot_data.index, plot_data.values, c=plot_data.values, cmap=plt.cm.cividis, s=6)
    ax.title.set_text(f"Lake {plot_data.name}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Mean Water Level (Meters)")
    ax.grid(True)
    
plt.tight_layout()
plt.show()

michigan_huron_max_min = (data.resample('Y')['Michigan-Huron'].agg(['min', 'max']))
lake_Superior_max_min = (data.resample('Y')['Superior'].agg(['min', 'max']))
lake_Erie_max_min = (data.resample('Y')['Erie'].agg(['min', 'max']))
lake_Ontario_max_min = (data.resample('Y')['Ontario'].agg(['min', 'max']))

year = np.arange(1917,2019)
plt.scatter(year, michigan_huron_max_min['min'])
plt.scatter(year, michigan_huron_max_min['max'])
plt.show()

#--------------------------------seaborn.heatmap---------------------------
#water_level = data.pivot("month", "year", "Michigan-Huron")
#months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

