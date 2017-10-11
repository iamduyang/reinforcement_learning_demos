# -*- coding:utf-8 -*-
"""
# Author:    Yang Du
# Email:     iamduyang (-A-T-) outlook dot com 
# Date:      2017-08-08
# Purpose:
#------------------------------------------------------------#
# Copyright (C) 2017       Yang DU
# This code is freely available for non-commercial purposes
#------------------------------------------------------------#
"""

import random

numberOf = 1000

def mc_pi(numbers):
    sum = 0
    for xx in range(0,numbers):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if (x*x+y*y)<=1:
        	sum = sum+1
    return 4.0*sum/numbers



	




if __name__ == "__main__":
    x = [100000,200000,300000,400000,500000]
    for xx in x:
        print(mc_pi(xx))

    print("end of work!")