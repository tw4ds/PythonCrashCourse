# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 19:10:25 2019

@author: Owner
"""

import matplotlib.pyplot as plt

input_values=[1,2,3,4,5,6]
squares=[1,4,9,16,25,36]
plt.style.use('fivethirtyeight')
fig, ax=plt.subplots()
ax.plot(input_values,squares,linewidth=3)

#set chart title and label axes
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Sqare of value",fontsize=14)

#set size oftick lables
ax.tick_params(axis='both',labelsize=14)
plt.show
