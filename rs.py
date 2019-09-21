#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 23:40:04 2019

@author: zjiezhang
"""

import functools as ft

#Roughset = rs(classes, Set)
#Using the set of sets 'classes' to approximate the set 'Set', and output a rough set

def rs(classes, Set):
    if isinstance(classes[0],set)==False:
        classes = list(map(lambda x: set(x), classes))
    if isinstance(Set,set)==False:
        Set = set(Set)
    
    apr_upper_list = list(filter(lambda x: len(Set.intersection(x))>0, classes))
    apr_low_list = list(filter(lambda x: Set.intersection(x) == x, classes))
    
    apr_upper = set(ft.reduce(lambda x,y: x.union(y), apr_upper_list))
    apr_low = set(ft.reduce(lambda x,y: x.union(y), apr_low_list))
    
    Roughset = [apr_low, apr_upper]
    return Roughset