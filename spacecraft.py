import gravity as gr
import math
import numpy as np
import matplotlib.pyplot as plt

class Spacecraft(gr.Gravity):

      def __init__(self,V0=[0], dt=0.1, t0=0,h=0.0,m=1.0):
         gr.Gravity.__init__(self,V0, dt, t0, h)
         self.m = m # When F is non null the mass plays a role
         
      def F(self,t,v):
          z,vz,phi,vphi=v[0],v[1],v[2],v[3]
          #define the thrust forces and set time dependence
          F_r=self.F_r
          if(t > self.t_thrust):
              F_r=0
          F_theta=self.F_theta
          if(t > self.t_thrust):
              F_theta=0
          
          eq_z =    vz
          eq_vz =   (-self.G*self.M_E)/(self.r_0 + z)**2 + (self.r_0 + z)*(self.omega_0 + vphi)**2 + F_r/self.m
          eq_phi =  vphi
          eq_vphi = (-2*(self.omega_0 + vphi)*vz)/(self.r_0 + z)+ F_theta/(self.m*(self.r_0 + z))
          return(np.array([eq_z,eq_vz,eq_phi,eq_vphi])) 

      def min_dist_to_target(self,Fr,Ftheta,t_thrust,tmax,dt,gdt=1):
          # ADD YOUR CODE HERE (store Fr,Ftheta, t_thrust in class variables ...)
          #store F_r, F_theta, t_thrust in class variables
##          """ Integrate equation and determine min distance to target
##          : param Fr     : radial thrust (perpendicular to orbit)
##          : param Ftheta : horizontal thrust (parralet to orbit)
##          : param t_thrust : duration of thrust
##          : param tmax : duration of integration
##          : param dt : integration time step
##          """
          self.F_r=Fr
          self.F_theta=Ftheta
          self.t_thrust=t_thrust

          #set initial conditions
          z0 =      -1000.
          v_z0 =    0.
          phi0=     -2000.0/self.r_0
          v_phi0=   math.sqrt(self.G*self.M_E*(self.r_0 + z0)**-3) - self.omega_0 #change
          self.reset([z0,v_z0,phi0,v_phi0],dt)
          self.iterate(tmax,gdt)
          return self.min_min()
       
        

if(__name__ == "__main__"):
    s = Spacecraft(h=4e5,m=4000.) # 4000kg spacecraft on 400km orbit
    tmax= 4000  #
    dt = 0.1
    def G(Fr,Ftheta,t_thrust):
          tmin,dmin = s.min_dist_to_target(Fr,Ftheta,t_thrust,tmax,dt)
          print ("F_r={} F_theta={} t_thrust={}".format(Fr,Ftheta,t_thrust))
          print ("dmin={}, tmin={} Fuel={}"\
          .format(dmin,tmin,(abs(Fr)+abs(Ftheta))*t_thrust))
    
    G(50.,100.,100.)
    s.plot(1,3,'b-') #plot labels

    G(25.,50.,200.)
    s.plot(1,3,'g-')

    G(10.,20.,500.)
    s.plot(1,3,'r-')

    plt.plot([0],[0],'c+')  
    plt.xlabel('phi',fontsize=20)
    plt.ylabel('z',fontsize=20)
    plt.show()
    
