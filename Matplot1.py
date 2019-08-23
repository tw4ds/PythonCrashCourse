# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 18:44:32 2019

@author: Owner
"""

import matplotlib.pyplot as plt

squares=[1,4,9,16,25,36]
fig, ax=plt.subplots()
ax.plot(squares,linewidth=3)

#set chart title and label axes
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Sqare of value",fontsize=14)

#set size oftick lables
ax.tick_params(axis='both',labelsize=14)
plt.show
