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
      #ADD YOUR CODE HERE

  def dist_2_reference(self):
      #ADD YOUR CODE HERE
  
  def post_integration_step(self):
      #ADD YOUR CODE HERE
      pass
      
  def min_min(self,t_after=0):
      #ADD YOUR CODE HERE
      pass
  

