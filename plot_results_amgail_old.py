#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 19:14:28 2018

@author: nick
"""

import numpy as np
import matplotlib.pyplot as plt
"""
def save_fig(itrs,means,stds, filepath="./graph_rewards.png",title = 'rewards vs itr',
             x_label="iteration", y_label="avg reward", x_range=(0, 1), y_range=(0,1), color="blue",  grid=True):
  fig = plt.figure()
  #ax = fig.add_subplot(111, autoscale_on=False, xlim=x_range, ylim=y_range)
  ax = fig.add_subplot(111, autoscale_on=True, xlim=x_range, ylim=y_range)
  ax.grid(grid)
  ax.set_xlabel(x_label)
  ax.set_ylabel(y_label)
  ax.set_title(title)
  ax.plot(itrs,means, color,  alpha=1.0)
  ax.fill_between(itrs,means+stds, means-stds, facecolor=color, alpha=0.5)
  fig.savefig(filepath)
  fig.clear()
  plt.close(fig)
  
  
def plot_fig(itrs,means,stds, filepath="./graph_rewards.png",title = 'rewards vs itr',
             x_label="iteration", y_label="avg reward", x_range=(0, 1), y_range=(0,1), color="blue",  grid=True):
  #ax = fig.add_subplot(111, autoscale_on=False, xlim=x_range, ylim=y_range)
  ax = fig.add_subplot(111, autoscale_on=True, xlim=x_range, ylim=y_range)
  ax.grid(grid)
  ax.set_xlabel(x_label)
  ax.set_ylabel(y_label)
  ax.set_title(title)
  ax.plot(itrs,means, color,  alpha=1.0)
  ax.fill_between(itrs,means+stds, means-stds, facecolor=color, alpha=0.5)
  fig.savefig(filepath)
  fig.clear()
  plt.close(fig)
"""

env_name = 'InvertedPendulum-v1'
skill = ['bad','mixed','good']
colors = ['red','blue','green']
linestyles = [':','--','-']
my_plots = []
fill_in = True

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=True)
ax.grid(True)
ax.set_xlabel('Iteration')
ax.set_ylabel('Average Reward')
ax.set_title(env_name+': Reward per Iteration using AMGAIL')

for i_skill in range(len(skill)):
    itrs = np.loadtxt('results/reward_itrs_'+skill[i_skill]+'_'+env_name+'_er.csv')
    means = np.loadtxt('results/reward_means_'+skill[i_skill]+'_'+env_name+'_er.csv')
    stds = np.loadtxt('results/reward_stds_'+skill[i_skill]+'_'+env_name+'_er.csv')
    my_plots.append(ax.plot(itrs,means,linestyle= linestyles[i_skill],color = colors[i_skill],alpha = 1))
    if fill_in == True:
        ax.fill_between(itrs,means+stds, means-stds, facecolor = colors[i_skill], alpha=0.5)

plt.legend(skill)
plt.show()



#%% testing
""" 
fig = plt.figure()
x = [1,2,3,4]
y4 = [4,4,4,4]
y6 = [6,6,6,6]

plt.plot(x,y4)
plt.plot(x,y6)

plt.show()
"""
