import math
from ode_RK4 import *
import gravity
import numpy
from numpy import *
import matplotlib.pyplot as plt

def min_dist(sigma,v,tmax,dt):
    b=gravity.Gravity(h=400000)
    b.v=[0,v*math.sin(sigma),-10000*(b.r_0**-1),v*math.cos(sigma)*(b.r_0**-1)]
    tmax=1500
    b.dt=dt
    b.integrate_until(tmax)
    return b.d_min

sig=[]
for i in numpy.linspace(-np.pi,np.pi,100):
    sig.append(i)
lists=[]
for x in range(0,100):
    lists.append(min_dist(sig[x],100,1500,0.1))
distances=[]
for x in lists:
    if x==[]:
        distances.append(x)
    else:
      distances.append(x[0][1])
      
print "Sigma for minimum distance:"
print sig[distances.index(min(distances))]
print "    "
print "Minimum distance:"
print min(distances)
print " "
print "Time for minimum distance:"
print lists[distances.index(min(distances))][0][0]


h = 400e3 # Altitude of reference trajectory
eq = gravity.Gravity(h)

def run(z0,v_z0,phi0,v_phi0):
    t0 = 0.0
    dt = 0.1
    t_max = 12000
    dt_grf = 10.0
    eq.init(t0,dt,[z0,v_z0,phi0,v_phi0]) 
    eq.integrate_trajectory_until(t_max,dt_grf) 
    plt.xlabel('phi',fontsize=20)
    plt.ylabel('z',fontsize=20)
    plt.plot(eq.plot_V[2],eq.plot_V[0],'-r');
    plt.show()

z0 = 0
v_z0= 100*math.sin(-0.1139)
phi0 = -10000.0/(eq.r_0)
v_phi0 = (100.0*math.cos(-0.1139))/(eq.r_0)
run(z0,v_z0,phi0,v_phi0)



    
    
