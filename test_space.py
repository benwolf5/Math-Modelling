# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 15:37:08 2019

@author: Ben's Laptop
"""

import gravity as gr
import math
import numpy as np
import matplotlib.pyplot as plt
from spacecraft import *

dt = 0.1
gdt = 1
s = Spacecraft([0,0,0,0],dt,0,4e5,4000.) # initial condition set later
tmax= 4000
Fr = 0
Ftheta = 100
t_thrust = 66.5

tmin,dmin = s.min_dist_to_target(Fr,Ftheta,t_thrust,tmax,dt,gdt)
print("Fr={} Ftheta={} t_thrust={}".format(Fr,Ftheta,t_thrust))
print("dmin={}, tmin={} Fuel={}"\
  .format(dmin,tmin,(abs(Fr)+abs(Ftheta))*t_thrust))
s.plot(1,3,'b-');
plt.xlabel('phi',fontsize=20)
plt.ylabel('z',fontsize=20)
plt.plot([0],[0],'r+');
plt.show()