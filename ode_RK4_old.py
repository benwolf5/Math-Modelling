# Solve a system of ODE   
# dy/dt = F(y)
# where F and y are N components vectors
import numpy as np

class ODE_RK4:
  def __init__(self):
      self.t = 0   # Integration variable
      self.dt = 0  # Integration step
      self.v = [0] # The functions for the equations
      # List used for plots: 
      #     import matplotlib.pyplot as plt
      #     eq = test_ode.test_ode()
      #     eq.init(0,0.01,np.array([0,1]))
      #     eq.integrate_until(0.1)
      #     eq.integrate_trajectory_until(10,0.1)
      #     plt.plot(eq.plot_t,eq.plot_V[0],"r-",eq.plot_t,eq.plot_V[1],"b-",)
      #     plt.show()
      self.plot_t = [] # list of time values for plots
      self.plot_V = [] # list of list of fct values for plots

  # THIS FUNCTION MUST BE CHANGED IN THE CHILD CLASS
  # returns the right hand side of the equation  
  # t : current time
  # v : curent fct value
  def F(self,t,v):
      return(np.array(-1.0*v))

  # THIS FUNCTION MUST BE CHANGED IN THE CHILD CLASS
  # Test for integrate_while and integrate_trajectory_while
  # Can use any test with self.t or self.v[i]
  def while_test(self,par):
      return (self.v[0] < par)

  # Executed after each integration step (at the ned of RK4_1step)
  # Can be used to track function values, compute extrema ...
  # TO BE OVERWRIDEN IN CHILD CLASS
  def post_integration_step(self):
      return()
     
  # Executed after each grf step in integrate_trajectory
  # Can be used to generate extra figures
  # TO BE OVERWRIDEN IN CHILD CLASS
  def extra_trajectory(self):
      return()

  # Initialise the paramaters (t, dt, v, initial cond.,  ...)
  def init(self,t,dt,v0):
      self.t = t
      self.dt = dt
      self.v = np.array(v0, dtype='float64') # ensure we use floats!
      self.plot_t = [self.t]  # time values for figures
      self.plot_V = []        # function values for figures
      for i in range(0,len(v0)): # create list of len(v0) init values
          self.plot_V.append([v0[i]])
      self.extra_trajectory() # 

  # Set the integration time step
  def set_dt(self,dt):
      self.dt = dt

  # Perform a single integration setp using
  # The 4th order Runge Kutta step.
  def RK4_1step(self):
      k1 = self.F(self.t,self.v) 
      self.K = self.v+0.5*self.dt*k1

      k2 = self.F(self.t+0.5*self.dt,self.K)
      self.K = self.v+0.5*self.dt*k2

      k3 = self.F(self.t+0.5*self.dt,self.K)
      self.K = self.v+self.dt*k3
 
      k4 = self.F(self.t+self.dt,self.K)
      self.v += self.dt/6.0*(k1+2.0*(k2+k3)+k4)
    
      self.t += self.dt # time is updated here
     
      self.post_integration_step() 

  # Perform n integration steps
  def integrate_step(self,n):
      while (n > 0):
         self.RK4_1step()
         n -= 1
      return(self.v)

  # Integrate until tmax is reached
  # does nothing else
  def integrate_until(self,tmax):
      while(self.t < tmax):
         self.RK4_1step()
      return(self.v)

  # Integrate until tmax is reached
  # Add data for trajectory in plot_t and plot_V
  # dt_grf : time interval between figure points
  def integrate_trajectory_until(self,tmax,dt_grf):
      if(dt_grf < self.dt) : dt_grf = self.dt
      next_tg = self.t+dt_grf
      while(self.t < tmax):
         self.RK4_1step()
         if(self.t > next_tg):
            self.plot_t.append(self.t)
            # append each item in corresponding list
            for i in range(0,len(self.v)): 
               self.plot_V[i].append(self.v[i])
            self.extra_trajectory() # do as above for extra figure data
            next_tg += dt_grf
      return(self.v)


  # Integrate equation while while_test(par) is true
  # Par : parameter for the test function
  def integrate_while(self,par):
      while(self.while_test(par)):
         self.RK4_1step()
      return(self.v)

  # Integrate equation while while_test(par) is true
  # Add data for trajectory in plot_t and plot_V
  # dt_grf : time interval between figure points
  def integrate_trajectory_while(self,par,dt_grf):
      if(dt_grf < self.dt) : dt_grf = self.dt
      next_tg = self.t+dt_grf # next time for figure output
      while(self.while_test(par)):
         self.RK4_1step()
         if(self.t > next_tg):
            self.plot_t.append(self.t)
            # append each item in corresponding list
            for i in range(0,len(self.v)): 
               self.plot_V[i].append(self.v[i])
            self.extra_trajectory()
            next_tg += dt_grf
      return(self.v)
