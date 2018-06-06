#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 23:59:52 2018

@author: nick
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 22:41:03 2018

@author: nick
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 19:14:28 2018

@author: nick
"""

import numpy as np
import matplotlib.pyplot as plt


#%% 

#env_names = ['Hopper-v1','HalfCheetah-v1','InvertedPendulum-v1']
env_names = ['HalfCheetah-v1','InvertedPendulum-v1']
for i_env in range(len(env_names)):    
    env_name = env_names[i_env]
    skill = ['bad','mixed','good']
    colors = ['red','blue','green']
    linestyles = ['-','-','-']
    my_plots = []
    fill_in = False
    
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=True)
    ax.grid(True)
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Average Reward')
    ax.set_title(env_name+': Reward using AMGAIL')
    min_max_x = 10000000000
    extra_x = 1.1
    for i_skill in range(len(skill)):
        itrs = np.loadtxt('results/reward_itrs_'+skill[i_skill]+'_'+env_name+'_er.csv')
        means = np.loadtxt('results/reward_means_'+skill[i_skill]+'_'+env_name+'_er.csv')
        stds = np.loadtxt('results/reward_stds_'+skill[i_skill]+'_'+env_name+'_er.csv')
        if itrs[-1] < min_max_x:
            min_max_x = itrs[-1]
            extra_itrs = np.arange(itrs[-1]+1,extra_x*itrs[-1])
            itrs_ext = np.hstack((itrs,extra_itrs))
            means_ext = np.hstack((means,means[-1]*np.ones(extra_itrs.shape[0])))
        else:
            itrs_ext = itrs
            means_ext = means
        my_plots.append(ax.plot(itrs_ext,means_ext,linestyle= linestyles[i_skill],color = colors[i_skill],alpha = 1,linewidth = 3))
        if fill_in == True:
            ax.fill_between(itrs,means+stds, means-stds, facecolor = colors[i_skill], alpha=0.5)
    
    plt.legend(skill)
    #plt.xlim((0,extra_x*min_max_x))
    plt.tight_layout()
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

#%% old 
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