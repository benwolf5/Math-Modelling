import gravity_kieran as gr
import math
import numpy as np
import matplotlib.pyplot as plt

class Spacecraft(gr.Gravity):

      def __init__(self,h=0.0,m=1.0):
          # we must initialise the h dependant parameters in Gravity
          gr.Gravity.__init__(self,h) 
          self.m = m # When F is non null the mass plays a role
          
      # The actual equation
      def F(self,t,v):
          z,vz,phi,vphi=v[0],v[1],v[2],v[3]
          F_r=self.F_r
          if(t > self.t_thrust): F_r=0
          F_theta=self.F_theta
          if(t > self.t_thrust): F_theta=0
          eq_z = vz
          eq_vz = (((-self.G*self.M_E)*((self.r_0+z)**-2))+((self.r_0+z)*((self.omega_0+vphi)**2))+(F_r*(self.m**-1)))
          eq_phi = vphi
          eq_vphi = ((-2*(self.omega_0+vphi)*vz*((self.r_0+z)**-1))+((F_theta)*((self.m*(self.r_0+z))**-1)))
          
          return(np.array([eq_z,eq_vz,eq_phi,eq_vphi]))  

      # Integrate equation and determine min distance to target
      # F_r     : radial thrust (perpendicular to orbit)
      # F_theta : horizontal thrust (parralet to orbit)
      # t_thrust : duration of thrust
      # tmax : duration of integration
      # dt : integration time step
      
      def min_dist_to_target(self,F_r,F_theta,t_thrust,tmax,dt):
          self.F_r=F_r
          self.F_theta=F_theta
          self.t_thrust=t_thrust
          z0 = -1000.0
          v_z0 = 0
          phi0= -2000.0/self.r_0
          v_phi0= math.sqrt((self.G*self.M_E)*((self.r_0+z0)**-3))-self.omega_0
          self.init(0.0,dt,[z0,v_z0,phi0,v_phi0]) 

          self.integrate_trajectory_until(tmax,1)
          self.d_min.append([tmax,self.dist_2_reference()])
          return(self.min_min())
    
if(__name__ == "__main__"):
    s = Spacecraft(h=4e5,m=4000.) # 4000kg spacecraft on 400km orbit
    tmax= 4000  #
    dt = 0.1
    #need to run for three cases
    def find_dis_time_fuel(F_r,F_theta,t_thrust,tmax,dt):
          tmin,dmin = s.min_dist_to_target(F_r,F_theta,t_thrust,tmax,dt)
          print "F_r={} F_theta={} t_thrust={}".format(F_r,F_theta,t_thrust)
          print "dmin={}, tmin={} Fuel={}"\
          .format(dmin,tmin,(abs(F_r)+abs(F_theta))*t_thrust)

    find_dis_time_fuel(50,100.,100,tmax,dt)
    plt.plot(s.plot_V[2],s.plot_V[0],'b-');
    
    find_dis_time_fuel(25,50.,200,tmax,dt)
    plt.plot(s.plot_V[2],s.plot_V[0],'g-');
    
    find_dis_time_fuel(10,20.,500,tmax,dt)
    plt.plot(s.plot_V[2],s.plot_V[0],'r-');

    plt.show()
    

    
