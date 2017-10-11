# -*- coding:utf-8 -*-
"""
# Author:    Yang Du
# Email:     iamduyang (-A-T-) outlook dot com 
# Date:      2017-08-08
# Purpose:

 k-armed Bandit softmax in RL

#------------------------------------------------------------#
# Copyright (C) 2017       Yang DU
# This code is freely available for non-commercial purposes
#------------------------------------------------------------#
"""

import random
import numpy
import math

k_number = 10
T = 100000
tau = 1



def reward_out(number_k):
    return random.uniform(0,number_k)

def generate_Q_array(number_k):
    return [0]*number_k

def generate_count_array(number_k):
    return [0]*number_k


def get_kk(Q_array,tau_array):
    probability_list =[]
    len_Q = len(Q_array)
    for x in range(len_Q):
        probability_list.append(math.e**(1.0*Q_array[x]/tau))
    

    sum_Q = sum(probability_list)
    for x in range(len_Q):
        probability_list[x] = probability_list[x]/sum_Q

    return_int_temp =numpy.random.choice(numpy.arange(0, len_Q), p=probability_list)

    return int(return_int_temp)


def k_armed_run(number_k,epsilon_now):
    acc_reward = 0
    count_array = generate_count_array(number_k)
    Q_array = generate_Q_array(number_k)
    for t in range(0,T):
        x = random.uniform(0,1)
        if random.uniform(0,1)<epsilon_now :
            kk = int(random.uniform(0,1)*number_k)
        else :
            kk = get_kk(Q_array)

        this_reward = reward_out(kk)
        acc_reward = acc_reward+this_reward
        Q_array[kk] = (Q_array[kk]*count_array[kk] + this_reward)*1.0/(count_array[kk]+1)
        count_array[kk] = count_array[kk]+1



    return acc_reward

	
def k_armed_run_more(number_k,tau_now):
    acc_reward = 0
    count_array = generate_count_array(number_k)
    Q_array = generate_Q_array(number_k)
    for t in range(0,T):
        x = random.uniform(0,1)

        kk = get_kk(Q_array,tau_array)

        this_reward = reward_out(kk)
        acc_reward = acc_reward+this_reward
        Q_array[kk] = (Q_array[kk]*count_array[kk] + this_reward)*1.0/(count_array[kk]+1)
        count_array[kk] = count_array[kk]+1
    return_array = [count_array,acc_reward]




    return return_array

def complex_result_print(result):
    print("total reward: %d"%(result[1]))
    a=result[0]
    for i in range(0,len(a)):
        print("%d: %d"%(i,a[i]))    


if __name__ == "__main__":
    tau_array =[]
    for x in range(1,10):
        tau_array.append(x*0.1)

    for x in tau_array:
        print('\ttau: %f'%x)
        result_cur = k_armed_run_more(k_number,x)
        complex_result_print(result_cur)





    print("end of work!")


