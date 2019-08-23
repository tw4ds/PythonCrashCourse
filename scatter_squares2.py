# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 19:22:39 2019

@author: Owner
"""

import matplotlib.pyplot as plt
xvalues = range(1,1001)
yvalues = [x**2 for x in xvalues]

plt.style.use('fivethirtyeight')
fig, ax=plt.subplots()
ax.scatter(xvalues,yvalues,c=yvalues,cmap=plt.cm.Blues,s=200)
ax.scatter(0,1100,0,110000)
plt.show