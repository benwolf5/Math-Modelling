import gravity as gr
import math
import numpy as np
import matplotlib.pyplot as plt

class Spacecraft(gr.Gravity):

      def __init__(self,V0=[0], dt=0.1, t0=0,h=0.0,m=1.0):
         gr.Gravity.__init__(self,V0, dt, t0, h)
         self.m = m # When F is non null the mass plays a role
         
      def F(self,t,v):
          ADD YOUR CODE HERE  

      def min_dist_to_target(self,Fr,Ftheta,t_thrust,tmax,dt,gdt=1):
        """ Integrate equation and determine min distance to target
          : param Fr     : radial thrust (perpendicular to orbit)
          : param Ftheta : horizontal thrust (parralet to orbit)
          : param t_thrust : duration of thrust
          : param tmax : duration of integration
          : param dt : integration time step
        """
        # ADD YOUR CODE HERE (store Fr,Ftheta, t_trust in class variables ...)
        z0 =      TO COMPLETE
        v_z0 =    TO COMPLETE
        phi0=     TO COMPLETE
        v_phi0=   TO COMPLETE
        TO COMPLETE
    
