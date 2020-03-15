# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 18:14:25 2019

@author: Ben's Laptop
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

height_data=pd.read_csv('data/AthmDensity.csv',index_col=0)
density_data=pd.read_csv('data/AthmDensity.csv',index_col=1)

h_mean=height_data.mean()
density_mean=density_data.mean()

