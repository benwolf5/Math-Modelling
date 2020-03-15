import gravity
import matplotlib.pyplot as plt
import math
import numpy as np

h = 4e5 # Altitude of reference trajectory
DGrav = gravity.Gravity(h) # Create gravity instance
t0 = 0
dt = 0.1
t_max = 1500
v=100
min_temp=[]
min_d=[[0,1e6]]


def min_dist(sigma,v,t_max,dt):   
    DGrav=gravity.Gravity(h=400000)
    DGrav.v=[0,v*math.sin(sigma),-10000*(DGrav.r_0**-1),v*math.cos(sigma)*(DGrav.r_0**-1)]
    tmax=1500
    DGrav.dt=dt
    DGrav.integrate_until(tmax)
    return DGrav.d_min

for sigma in np.linspace(-np.pi,np.pi,100):
    min_temp= min_dist(sigma,100,1500,0.1)
    if min_temp!=[]:
        if min_temp[0][1]<min_d[0][1]:
            min_d=min_temp
            min_sigma=sigma         
            
print "Sigma for minimum distance:", min_sigma,
print "  "
print "Minimum distance:",min_d[0][1]
print "Time for minimum distance:",min_d[0][0]
         
def run(z0,v_z0,phi0,v_phi0):
    # integration parameters
    t0 = 0
    dt = 0.1
    t_max = 12000
    dt_grf = 10
    DGrav.init(t0,dt,[z0,v_z0,phi0,v_phi0]) 
    # Integrate until t_max
    DGrav.integrate_trajectory_until(t_max,dt_grf) 
    # Plot z(phi)
    plt.xlabel('phi',fontsize=20)
    plt.ylabel('z',fontsize=20)
    plt.plot(DGrav.plot_V[2],DGrav.plot_V[0],'-r');
    plt.show()


sigma=-0.1139
z0=0
v_z0=v*math.sin(sigma)
phi0=-10000.0*(DGrav.r_0**-1)
v_phi0=v*math.cos(sigma)*(DGrav.r_0**-1)
run(z0,v_z0,phi0,v_phi0)