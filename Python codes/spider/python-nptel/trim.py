# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:00:08 2022

@author: Pratik
"""

from statistics import mean

estimates=[100,200,500,250,180,300]
estimates.sort()
tv=int(0.1*len(estimates))
estimates=estimates[tv:]
print(mean(estimates))


from scipy import stats

m=stats.trim_mean(estimates,0.1)
print(m)


import matplot.pyplot as plt

plt.plot([1,2,3,4],[4,6,7,11])
