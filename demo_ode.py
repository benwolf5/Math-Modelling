from ode_rk4 import *
import matplotlib.pyplot as plt


class Demo_ode(ODE_RK4):
  def __init__(self, k=1):
      ODE_RK4.__init__(self) # we can miss this out
      self.k = k
      self.Fx = 0

# initialise the force variable
# Fx : force amplitude
# t_trust : duration of force impulse
  def set_Fx(self, Fx, t_thrust):
      self.Fx=Fx
      self.t_thrust = t_thrust
    
# equation to solve: 
#        d^2x/dt^2 = -k Fx    
# is equivalent to
#        dx/dt= v_x
#        dv_x/dt = -k x + Fx
# Time dependant force:
#    Fx = self.Fx  if t <= t_thrust
#    Fx = 0        if t > t_thrust
# t: current time
# v: current function as a vector
#    v[0] is f  and v[1] is g=df/dt
###########################################
  def F(self, t, v):
      Fx = self.Fx
      if(t > self.t_thrust): Fx=0
      eq_x = v[1]
      eq_vx = -self.k*v[0]+Fx
      return(np.array([eq_x,eq_vx]))
   
if (__name__== "__main__"):
  # ceate and initialise  Demo_ode
  eq = Demo_ode(1.0)
  Fx = 0.1
  t_thrust = 2
  eq.set_Fx(Fx,t_thrust)  # the the force parameters
  t0 = 0 # initial values
  x0 = 0
  vx0 = 0
  dt = 0.01 # integration time step
  t_max = 20 
  fig_dt = 0.1 # interval between figure points
  eq.reset([x0,vx0],dt,t0) # Set initial conditions: start at rest
  eq.iterate(t_max,fig_dt) # Integrate from 0 to tmax
  plt.xlabel('t')
  plt.ylabel('x, v_x')
  # plot f(t) and g(t)
  eq.plot(1, 0, style="b-")
  eq.plot(2, 0, style="r-")
  plt.show() # x is blue and v_x is red
  # plot phase space: g(t) as a function of f(t)
  plt.plot(eq.plot_V[0],eq.plot_V[1],'-g');
  plt.show() # x is blue and v_x is red
  
