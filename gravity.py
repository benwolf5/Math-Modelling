from ode_rk4 import *
import math

class Gravity(ODE_RK4):
  def __init__(self,V0=[0], dt=0.1, t0=0,h=0.0):
      """ V0 : initial conditions for z, v_z, phi, v_phi.
          dt : integration time step
          t0 : initial time
          h : altitude of the target orbit
      """
      super().__init__(V0,dt,t0)
      self.h = h
      self.G = 6.673e-11
      self.M_E = 5.97e24
      self.R_E = 6370e3
      self.r_0 = self.R_E+h
      self.omega_0 = math.sqrt(self.G*self.M_E/self.r_0**3)
      self.F_r = 0
      self.F_theta = 0
      self.m = 1
      self.t_last = 0
      self.d_last = -1
      self.d_butlast = -1
      self.d_min = []
      self.d_max = []

  def reset(self, V0, dt, t0=0):
      """ Reset the integration parameters; see __init__ for more info."""
      super().reset(V0, dt, t0)
      self.t_last = 0
      self.d_last = -1
      self.d_butlast = -1
      self.d_min = []
      self.d_max = []

      
###########################################################################
# COMPLETE THE CLASS FUNCTIONS BELOW
###########################################################################
      
  def F(self,t,v):
      """ Equation to solve: 
          v[0] is z
          v[1] is dz/dt
          v[2] is phi
          v[3] is dphi/dt
      """
      z,vz,phi,vphi=v[0],v[1],v[2],v[3]
      eq_z =    vz
      eq_vz =   ((-self.G*self.M_E)/((self.r_0+z)**2)) + ((self.r_0+z)*((self.omega_0+vphi)**2))+(self.F_r/self.m)
      eq_phi =  vphi
      eq_vphi = ((-2*(self.omega_0+vphi)*vz)/(self.r_0+z))+self.F_theta/(self.m*(self.r_0+z))
      #self.v=np.array([eq_z,eq_vz,eq_phi,eq_vphi])
      return(np.array([eq_z,eq_vz,eq_phi,eq_vphi]))


  def dist_2_reference(self):
      return math.sqrt((self.V[0]**2)+(2*self.r_0*(self.r_0+self.V[0])*(1-math.cos(self.V[2])))) 
  
  def post_integration_step(self):
      d = self.dist_2_reference()
      if len(self.d_min) < 3:  #Can only run this after 3 points
        self.d_min.append([self.t_last,d])
        self.d_max.append([self.t_last,d])
        pass
      if (self.d_butlast > self.d_last) and (self.d_last < d) : #local min
           self.d_min.append([self.t_last,self.d_last])
      elif (self.d_butlast < self.d_last) and (self.d_last > d) : #local max
           self.d_max.append([self.t_last,self.d_last])
      self.d_butlast = self.d_last
      self.d_last = d
      self.t_last = self.t
      
  def min_min(self,t_after=0):
      if self.d_min == []: 
          return [] # no minimum
      min_val = [] #  [ tmin, d_min]
      n = 0
      for minlists in self.d_min: # scan all but the first item
        if minlists[0] >= t_after :
          if n==0:
            min_val = list(minlists) # make a copy of the list
            n += 1
          elif minlists[1] < min_val[1]:
            min_val = list(minlists) # make a copy of the list
            n+=1
        else:
          return [] #no min after t_after
      return min_val

