import numpy as np
import os
from environment import Environment
from driver import Driver

import matplotlib.pyplot as plt


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
  
def dispatcher(env, ER_name):

    driver = Driver(env,ER_name)
    driver_itrs = []


    while driver.itr < env.n_train_iters:

        # Train
        if env.train_mode:
            driver.train_step()

        # Test
        if (driver.itr % env.test_interval -env.test_interval) > -100:
            print("about to record")
        if driver.itr % env.test_interval == 0:
            print("iteration"+str(driver.itr))
            # measure performance
            R = []
            for n in range(env.n_episodes_test):
                R.append(driver.collect_experience(record=True, vis=env.vis_flag, noise_flag=False, n_steps=1000))

            # update stats

            driver.reward_mean = float(sum(R)) / len(R)
            driver.reward_std = np.std(R)
            
            #save running rewards and stds
            driver_itrs.append(driver.itr)
            driver.reward_mean_Arr.append(driver.reward_mean)
            driver.reward_std_Arr.append(driver.reward_std)
            
            save_fig(np.array(driver_itrs),np.array(driver.reward_mean_Arr),np.array(driver.reward_std_Arr) ,'results/rewards_plot_'+ER_name+'.png', my_ER_name,'iteration','avg_reward')
            
            np.savetxt('results/reward_itrs_'+ER_name+'.csv', np.array(driver_itrs), delimiter=",")
            np.savetxt('results/reward_means_'+ER_name+'.csv', np.array(driver.reward_mean_Arr), delimiter=",")
            np.savetxt('results/reward_stds_'+ER_name+'.csv', np.array(driver.reward_std_Arr), delimiter=",")
            
            #np.save('reward_itrs_hop.npy',np.array(driver_itrs))
            #np.save('reward_means_hop.npy',np.array(driver.reward_mean_Arr))
            #np.save('reward_stds_hop.npy',np.array(driver.reward_std_Arr))
            
            # print info line
            driver.print_info_line('full')

            # save snapshot
            if env.train_mode and env.save_models:
                driver.save_model(dir_name=env.config_dir)

        driver.itr += 1


if __name__ == '__main__':
    # load environment
    my_env_name = 'Hopper-v1'
    my_ER_name = 'good_'+my_env_name+'_er'

    env = Environment(os.path.curdir, my_env_name, my_ER_name)

    # start training
    dispatcher(env=env,ER_name = my_ER_name)
