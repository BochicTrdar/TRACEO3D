#==================================================================
#  
#  TRACEO3D: Pekeris flat waveguide
#  Faro, Seg 11 Abr 2022 11:30:56 WEST 
#  Written by Tordar
#  
#==================================================================

from os import *
import sys
from wtraceo3dinfil import *
from numpy import *
from scipy.io import *
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

system("rm -rf rco.mat")

print('Pekeris waveguide test:')

case_title = "Pekeris waveguide & ray calculations"

#==================================================================
#  
#  Define source data:
#  
#==================================================================

freq = 125.0; ray_step = 5.0
zs   =  74.2
xs   = array([0.0,0.0,zs])

nthetas = 11; thetamin = -14; thetamax = 14
thetas = linspace(thetamin,thetamax,nthetas)

phi = array([-30.0, 0.0, 30.0]); nphi = phi.size

rmax = 1898.0
xbox = array([-rmax,rmax])
ybox = array([-rmax,rmax])

source_data = {"ds":ray_step, "position":xs, "xbox":xbox, "ybox":ybox, "f":freq,"thetas":thetas,"nthetas":nthetas,
              "phi":phi, "nphi":nphi}

#==================================================================
#  
#  Define altimetry data:
#  
#==================================================================

btype = 'V' 
ptype = 'H'
itype = 'FL'
x     = array([-rmax-1.0, rmax+1.0])
y     = array([-rmax-1.0, rmax+1.0])
z     = zeros((2,2))
units = 'W'
properties = zeros(5)

surface_data = {"btype":btype, "ptype":ptype, "units":units,"itype":itype,"x":x,"y":y,"z":z,"properties":properties}

#==================================================================
#  
#  Define sound speed data:
#  
#==================================================================

Dmax =  152.1
c0   = 1482.0

x = zeros(1)
y = zeros(1)
z = array([0.0,Dmax])
c = array([c0,c0])

ssp_data = {"ctype":"ISOV","x":x,"y":y,"z":z,"c":c}

#==================================================================
#  
#  Define bathymetry data:
#  
#==================================================================

btype = 'E' 
ptype = 'H'
itype = 'FL'
x     = array([-rmax-1.0, rmax+1.0])
y     = array([-rmax-1.0, rmax+1.0])
z     = Dmax*ones((2,2))
units = 'W'

properties = array([2290.0, 1050.0, 1.378, 0.76, 1.05])

bottom_data = {"btype":btype, "ptype":ptype, "units":units,"itype":itype,"x":x,"y":y,"z":z,"properties":properties}

#==================================================================
#  
#  Define output data:
#  
#==================================================================

xarray = zeros(1)
yarray = zeros(1)
zarray = zeros(1)

nxa = 1
nya = 1
nza = 1

miss = 0.5

output_data = {"ctype":"RCO","array_shape":"VRY","x":xarray,"y":yarray,"z":zarray,
               "nxa":nxa,"nya":nya,"nza":nza,"miss":miss}

print('Writing TRACEO3D waveguide input file...')

wtraceo3dinfil("pekeris.in",case_title,source_data,surface_data,ssp_data,bottom_data,output_data)

system('traceo3d.exe pekeris.in');

print('Reading the output data...')

data = loadmat('rco.mat')

fig = figure(1)
ax = fig.add_subplot(111, projection="3d")

for i in range(1,nthetas*nphi+1):

   if i < 10:
      rayname = 'ray0000' + str(i)
   elif i < 100:
      rayname = 'ray000'  + str(i)
   elif i < 1000:
      rayname = 'ray00'   + str(i)
   elif i < 10000:
      rayname = 'ray0'    + str(i)
   else:
      rayname = 'ray'     + str(i)   

   rayi = data[rayname]
   
   x = rayi[0,]
   y = rayi[1,]   
   z = rayi[2,]
   ax.plot(x,y,-z)
   
#ax.text(xs[0], xs[1], -xs[2], "*", color='blue' , ha='center', va='center')
ax.text(xs[0], xs[1], -xs[2], "o", color='black', ha='center', va='center',fontsize=16)   
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
title('TRACEO3D - Pekeris waveguide, ray trajectories')   
show()

print('done.')
