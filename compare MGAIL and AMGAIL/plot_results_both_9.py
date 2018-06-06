#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 00:52:32 2018

@author: nick
"""

import numpy as np
import matplotlib.pyplot as plt


#%% 

#env_names = ['Hopper-v1','HalfCheetah-v1','InvertedPendulum-v1']
env_names = ['InvertedPendulum-v1','Hopper-v1','HalfCheetah-v1',]
skills = ['bad','mixed','good']
Tiers = ['Tier 3','Tier 2', 'Tier 1']
alg = ['MGAIL','AMGAIL']
colors = ['red','blue']
linestyles = ['-','-']
fill_in = True

i_fig = 0
for i_env in range(len(env_names)):
    env_name = env_names[i_env]
    for i_skill in range(len(skills)):
        skill = skills[i_skill]
        fig = plt.figure()
        ax = fig.add_subplot(111, autoscale_on=True)
        ax.grid(True)
        ax.set_xlabel('Iteration')
        ax.set_ylabel('Average Reward')
        ax.set_title(env_name+' '+Tiers[i_skill]+': Reward Comparison')
        
        #for cutting off x axis
        min_max_x = 10000000000
        extra_x = 1.1
        
        #begin
        itrs_M = np.loadtxt('results_M/reward_itrs_'+skill+'_'+env_name+'_er.csv')
        means_M = np.loadtxt('results_M/reward_means_'+skill+'_'+env_name+'_er.csv')
        stds_M = np.loadtxt('results_M/reward_stds_'+skill+'_'+env_name+'_er.csv')
        
        itrs_A = np.loadtxt('results_A_David/reward_itrs_'+skill+'_'+env_name+'_er.csv')
        means_A = np.loadtxt('results_A_David/reward_means_'+skill+'_'+env_name+'_er.csv')
        stds_A = np.loadtxt('results_A_David/reward_stds_'+skill+'_'+env_name+'_er.csv')
        
        if i_fig ==1: #extend A for this one
            extra_itrs = np.arange(itrs_A[-1]+1,itrs_M[-1])
            itrs_A = np.hstack((itrs_A,extra_itrs))
            means_A = np.hstack((means_A,means_A[-1]*np.ones(extra_itrs.shape[0])))
            stds_A = np.hstack((stds_A,np.zeros(extra_itrs.shape[0])))
        
            #add similar for std
        ax.plot(itrs_M,means_M,linestyle= linestyles[0],color = colors[0],alpha = 1,linewidth = 3)
        if fill_in == True:
            ax.fill_between(itrs_M,means_M+stds_M, means_M-stds_M, facecolor = colors[0], alpha=0.5)
        
        ax.plot(itrs_A,means_A,linestyle= linestyles[1],color = colors[1],alpha = 1,linewidth = 3)
        if fill_in == True:
            stds_A = stds_A[:itrs_A.shape[0]]
            ax.fill_between(itrs_A,means_A+stds_A, means_A-stds_A, facecolor = colors[1], alpha=0.5)
        
        plt.legend(alg)
        #plt.xlim((0,extra_x*min_max_x))
        plt.tight_layout()
        plt.show()
        
        i_fig +=1



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