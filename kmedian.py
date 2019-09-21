#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 23:01:28 2019

@author: zjiezhang
"""

import numpy as np

epsilon = 0.0000000000001 #a very small value to ensure that the denominator is not zero

def dis(data,V):
    dis = list(map(lambda x: list(map(lambda v: np.linalg.norm(x - v), V)), data))
    return np.array(dis)

def kmedians(data,k,threshold):
    data = np.array(data)
    V=data[np.random.randint(0,len(data),k)]+epsilon
    diff = 10000
    U = []
    
    while diff>threshold:
        pdist = dis(data,V)
        U = np.array(list(map(lambda x: x<=np.min(x), pdist)))
        
        #update the new centers
        clusters = np.array(list(map(lambda x: data[U[:,x]==True],range(0,k))))
        Vnew = np.array(list(map(lambda x: np.median(x.T,1), clusters)))
        
        diff = max(sum(((V-Vnew)*(V-Vnew)).T))
        V=Vnew
        print(diff)

    return [U,V]