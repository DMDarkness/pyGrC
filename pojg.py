#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:15:34 2019

@author: zjiezhang
"""

import numpy as np

#the principle of justifiable granularity where the modal is defined as median and the specificity is defined as exp(-alpha*length)
#data: the data to be granulated, which is a list of elements where every element is a number
#      if element is number, the granule looks (lowerbound, modal, upperbound)
#alpha: the parameter to control the importance of specificity
def pojgMedE(data, alpha):
    data = np.array(data)
    lb = 0
    modal = 0
    ub = 0
#    if data.size == len(data):
    data = np.sort(data)
    
    #computing the modal
    modal = np.median(data)
    
    #split the dataset by the modal
    uparray = data[data>modal]
    lwarray = data[data<modal]
    
    #computing the specificity
    upsp = np.exp(-alpha*(uparray - modal))
    lwsp = np.exp(-alpha*(modal - lwarray))
    
    #computing the coverage
    upcov = np.array(range(1,len(upsp)+1))
    lwcov = len(lwsp) - np.array(range(0,len(lwsp)))
    
    #computing the performance
    upper = upcov*upsp
    lwper = lwcov*lwsp
    
    #selecting the lower bound and upper bound
    ub = uparray[np.argmax(upper)]
    lb = lwarray[np.argmax(lwper)]
    
    return [lb,modal,ub]
#    else:
#        modal = map(lambda x: np.median(data[:,x]), range(0,len(data[0])))
#        modal = np.array(list(modal))       
#        dis = np.array(list(map(lambda x: np.linalg.norm(x - modal), data)))       
#        dis = np.sort(dis)
#        
#        sp = np.exp(-alpha*dis)
#        cov = np.array(range(1,len(sp)+1))
#        
#        per = cov*sp
#        r = dis[np.argmax(per)]
#
#        return [modal, r]
