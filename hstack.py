# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:41:25 2020

@author: KIRAN HP
"""
"""
51   53   71
59   49   52
51   50   58
55   55   67
60   55   38
54   56   64
91   69   81
91   76   79
"""
import numpy as np
sem3=np.array([51,59,51,55,60,54,91,91])
sem4=np.array([53,49,50,55,55,56,69,76])
print(np.hstack((sem3,sem4)))

