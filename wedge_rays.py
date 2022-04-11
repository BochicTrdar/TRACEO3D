#==================================================================
#  
#  TRACEO3D: LMA CNRS Experimental Data
#  Faro, Seg 11 Abr 2022 19:50:19 WEST 
#  Written by Tordar
#  
#==================================================================

from os import *
import sys
from wtraceo3dinfil import *
from numpy import *
from scipy.io import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D

system("rm -rf rco.mat")

print('LMA CNRS Tank Experiment:') 

case_title = "LMA_CNRS_Tank_Experiment"

#==================================================================
#  
#  Define source data:
#  
#==================================================================

slope = 4.55
k = tan( slope*pi/180 ); z0 = 44.4
x1 = -z0/k;
x2 =   -x1;
z1 = k*x1 + z0;
z2 = k*x2 + z0;
zmax = max([z1,z2])

freq = 150.0; ray_step = 1.0
zs   = 8.3
xs   = array([0.0,0.0,zs])

nthetas = 11; thetamin = -15; thetamax = 15
thetas = linspace(thetamin,thetamax,nthetas)


phi = arange(90,111,1); nphi = phi.size

xbox = array([-400,400])
ybox = array([-100,5000])

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
x     = array([x1,x2])
y     = array([-100,6000])
z     = zeros((2,2))
units = 'W'
properties = zeros(5)

surface_data = {"btype":btype, "ptype":ptype, "units":units,"itype":itype,"x":x,"y":y,"z":z,"properties":properties}

#==================================================================
#  
#  Define sound speed data:
#  
#==================================================================

c0 = 1488.2 # Page 113

x = zeros(1)
y = zeros(1)
z = array([0.0,z2])
c = array([c0,c0])

ssp_data = {"ctype":"ISOV","x":x,"y":y,"z":z,"c":c}

#==================================================================
#  
#  Define bathymetry data:
#  
#==================================================================

xbty = array([x1,x2])
ybty = array([-100,6000])
zbty = array([[z1,z2],[z1,z2]])

btype = 'E' 
ptype = 'H'
itype = '2P'
x     = xbty
y     = ybty
z     = zbty
units = 'W'

properties = array([1700, 0, 1.99, 0.5, 0])

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

wtraceo3dinfil("lmacnrs.in",case_title,source_data,surface_data,ssp_data,bottom_data,output_data)

system('traceo3d.exe lmacnrs.in')

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

ax.text(xs[0], xs[1], -xs[2], "o", color='black', ha='center', va='center',fontsize=16)   
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
show()

print('done.')
