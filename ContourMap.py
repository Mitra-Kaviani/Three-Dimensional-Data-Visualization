#importing necessary libraries
import pandas as pd
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import matplotlib.cm as cm

#Read input file from dircetory
df_xyz = pd.read_csv('C:/.....csv')

#Define variables
x = df_xyz.iloc[:,0].values
y = df_xyz.iloc[:,1].values
z = df_xyz.iloc[:,2].values

#Define contour plot function
def plot_contour(x,y,z,resolution = 100,contour_method='linear'):
    resolution = str(resolution)+'j'
    X,Y = np.mgrid[min(x):max(x):complex(resolution),   min(y):max(y):complex(resolution)]
    points = [[a,b] for a,b in zip(x,y)]
    Z = griddata(points, z, (X, Y), method=contour_method)
    return X,Y,Z

X,Y,Z = plot_contour(x,y,z,resolution = 100,contour_method='linear')

#***--------Ploting Contour--------***--------------------
#set the contour levels
levels = [0,0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
#set scater plot behind
plt.scatter(x,y, color="black", linewidth=1, edgecolor="none", s=50)  
#plot the contour
contour = plt.contour(X, Y, Z, levels, colors='k') 
#add number and editing options for contour levels 
plt.clabel(contour, colors = 'k', fmt = '%2.1f', fontsize=10)
#set individual color for contour levels
c= ('#363093','#069ccf','#37b89d','#a5be6a','#fdbe3d','#f8fa0d','#f80000')
#fill color between contour levels  
contour_filled = plt.contourf(X, Y, Z, levels, colors=c) 
plt.colorbar(contour_filled)
plt.scatter(x,y, color="black", linewidth=1, edgecolor="none", s=10)
plt.title('Zeta v. Flow and Speed with Channel')# set title for the plot 
plt.xlabel('$\omega$ (RPM)') # add lable for x
plt.ylabel('Q (L/s)') # add lable for y
plt.xlim(20, 80)# change the data range for x
plt.ylim(6, 10)# change the data range for y
plt.show() #


#Refrences
##https://stackoverflow.com/questions/52935143/how-to-do-a-contour-plot-from-x-y-z-coordinates-in-matplotlib-plt-contourf-or
###https://www.python-course.eu/matplotlib_contour_plot.php


