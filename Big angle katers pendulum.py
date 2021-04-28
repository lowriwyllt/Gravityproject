# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:23:19 2021

@author: Lowri
"""
#import libaries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

#Times imported from excel file
times = pd.read_excel('Reversible pendulum all data .xlsx', sheet_name="times")
x2 = times["x2"].dropna(); #x in meters
T_1_2 = times["t1_2"].dropna(); #t1 in seconds
T_2_2 = times["t2_2"].dropna(); #t2 in seconds


##METHOD 1 - intercepts 
#line for wehn needing to plot best fit
l_line = np.linspace(0.63, 0.77, 100)

#quadratic equation for time period
def periodT(l, a, b, c):
    return (a*(l**2)) + (b*l) + c

popt_T1, pcov_T1 = curve_fit(periodT, x2, T_1_2)
popt_T2, pcov_T2 = curve_fit(periodT, x2, T_2_2)

print("equation for T1 is: ", (popt_T1[0]), "l^2 + ",(popt_T1[1]),"l + ",(popt_T1[2]))
print("equation for T2 is: ", (popt_T2[0]), "l^2 + ",(popt_T2[1]),"l + ",(popt_T2[2]))

#intercepts when T1 and T2 are equal
l1 = 0.7306449629153
l2 = 0.57145800340423

print("when l = ", l1, "then T1 = ", periodT(l1, popt_T1[0], popt_T1[1], popt_T1[2]))
print("when l = ", l1, "then T2 = ", periodT(l1, popt_T2[0], popt_T2[1], popt_T2[2]))
print("when l = ", l2, "then T1 = ", periodT(l2, popt_T1[0], popt_T1[1], popt_T1[2]))
print("when l = ", l2, "then T2 = ", periodT(l2, popt_T2[0], popt_T2[1], popt_T2[2]))

T = 2.01
angle = 16*np.pi/180

g = 0.9939/((T/(2*np.pi*(1+((1/16)*angle**2)+(11/3072)*angle**4)))**2)
print("g =", g, " for when T =", T )

# Create a "figure" and set its aspect ratio. Play with the numbers to make it square, or long or short. 
fig = plt.figure() #figsize=(7,7)
# Here we only want one plot in the figure to a 1 by 1 set of plots and this is number 1. Leave alone for now. 
ax = fig.add_subplot(111)
ax.set_xlim(0.64, 0.76)
ax.set_ylim(1.975, 2.03)
plt.plot(l_line, periodT(l_line, popt_T1[0], popt_T1[1], popt_T1[2]) , "-k")
plt.plot(l_line, periodT(l_line, popt_T2[0], popt_T2[1], popt_T2[2]) , "-k")
# This nest bit does a lot of work and plots a graph with error bars.
ax.errorbar(x2,           # x coordinates
             T_1_2,              # y coordinates
             yerr = (0.2/50),     # y errors
             xerr = 0.002,
             marker='o',             # marker used is a cicle 'o'. Could be crosses 'x', or squares 's', or 'none'
             markersize = 7,        # marker size
             color='r',          # overall colour I think ( red)
             ecolor='r',         # edge colour for you marker (red)
             markerfacecolor='r', # red
             linestyle='none',       # no line joining markers, could be a line '-', or a dashed line '--'
             capsize=6,              # width of the end bit of the error bars, not too small nor too big please.
             )

ax.errorbar(x2,           # x coordinates
             T_2_2,              # y coordinates
             yerr = (0.2/50),     # y errors
             xerr = 0.002,
             marker='x',             # marker used is a cicle 'o'. Could be crosses 'x', or squares 's', or 'none'
             markersize = 7,        # marker size
             color='black',          # overall colour I think
             ecolor='black',         # edge colour for you marker
             markerfacecolor='black',
             linestyle='none',       # no line joining markers, could be a line '-', or a dashed line '--'
             capsize=6,              # width of the end bit of the error bars, not too small nor too big please.
             )
plt.xlabel('l$_1$ of movable mass (m) ', fontsize = 20, fontname='Times New Roman' )
plt.ylabel('Time period (s)', fontsize = 20, fontname='Times New Roman')
plt.show()