from ode_RK4 import *
import math

class Gravity(ODE_RK4):
  def __init__(self,h=0.0):
      ODE_RK4.__init__(self) 
      self.reset()
      #ADD YOUR PARAMETER VARIABLES HERE
      self.G=6.673e-11
      self.M_E=5.97e24
      self.R_E=6370000
      self.r_0=self.R_E+h
      self.omega_0=math.sqrt(self.G*self.M_E*(self.r_0**-3))
      self.m=1
      self.F_r=0
      self.F_theta=0

  def reset(self):
      # init variable to keep track of local minima and maxima
      self.t_last = 0
      self.d_last = -1
      self.d_llast = -1
      self.d_min = []
      self.d_max = []
      
# equation to solve: 
#    d**2z/dt**2 =  - G M_E/r**2+r*dtheta**2+F_r/m  
#    d**2phi/dt**2 = -2*(dphi/dt+omega_0)*dz/dt/r+F_theta/(m r) 
# t: current time 
# v: current function as a vector
#    v[0] is z   and v[1] is vz=dz/dt
#    v[2] is phi and v[3] is vphi=dphi/dt
###########################################
  def F(self,t,v):
      z,vz,phi,vphi=v[0],v[1],v[2],v[3]
      eq_z = vz
      eq_vz = (((-self.G*self.M_E)*((self.r_0+z)**-2))+((self.r_0+z)*((self.omega_0+vphi)**2))+((self.F_r)*((self.m)**-1)))
      eq_phi = vphi
      eq_vphi = ((-2*(self.omega_0+vphi)*vz*((self.r_0+z)**-1))+((self.F_theta)*((self.m*(self.r_0+z))**-1)))
      return(np.array([eq_z,eq_vz,eq_phi,eq_vphi]))

  # computes the distance between this object and the reference
  # trajectory on a circular orbit
  def dist_2_reference(self):
      return math.sqrt((2*self.r_0*(self.r_0+self.v[0])*(1-math.cos(self.v[2])))+(self.v[0]**2))
  
  # Runs after every integration step.
  # track the extremum values of x
  def post_integration_step(self):
      d = self.dist_2_reference()
      if (self.d_llast > self.d_last) and (self.d_last < d) : #local min
           self.d_min.append([self.t_last,self.d_last])
      elif (self.d_llast < self.d_last) and (self.d_last > d) : #local max
           self.d_max.append([self.t_last,self.d_last])
      self.d_llast = self.d_last
      self.d_last = d
      self.t_last = self.t
   
  # compute smalest minimum ignoring minima occuring before t_after
  def min_min(self,t_after=1e-20):
      if self.d_min == []: return [] # no minimum
      min_val = [] #  [ tmin, d_min]
      n = 0;
      for v in self.d_min: # scan all but the first item
         if v[0] > t_after :
           if n==0:
              min_val = list(v) # make a copy of the list
              n += 1
           elif v[1] < min_val[1]:
              min_val = list(v) # make a copy of the list
      return(min_val)
  
