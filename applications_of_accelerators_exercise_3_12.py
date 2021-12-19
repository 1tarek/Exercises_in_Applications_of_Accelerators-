'''
12.	From the accelerator department, you received some data (see the attached 
data file: 2016-07-11_ipm_data.txt) from an ionisation beam profile monitor 
(IPM). Read the file and plot it in blue color on a black grid background. 
Then mark the maximum with a red dot! Code and plot (PNG) as usual on GitHUB.
'''


import numpy as np
import matplotlib.pyplot as plt


#get the data
data1=np.genfromtxt('2016-07-11_imp_data.txt', delimiter='e+0')
data2=data1[:,0]*10 #replace the missing magnitude
n=len(data2)


#determine the maximum value
maximum=0
for i in range(n):
    if data2[i]>maximum:
        maximum=data2[i]
        index=i


#plot the data
plt.plot(data2)
plt.xlabel(r'position')
plt.ylabel(r'signal')
plt.title(r'ionisation beam profile monitor data')
plt.grid(color='k') #grid in black
plt.plot(index, maximum, marker='o', mfc='r') #add red dot at maximum
plt.savefig('Tareks_plot.png') #save image as png


