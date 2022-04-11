#==================================================================
#  
#  TRACEO3D: LMA CNRS Experimental Data
#  Faro, Seg 11 Abr 2022 19:50:35 WEST 
#  Written by Tordar
#  
#==================================================================

from os import *
import sys
from wtraceo3dinfil import *
from numpy import *
from scipy.io import *
from matplotlib.pyplot import *

system("rm -rf cpr.mat")

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

nthetas = 390; thetamin = -45; thetamax = 45
thetas = linspace(thetamin,thetamax,nthetas)


phi = arange(90,110.1,0.1); nphi = phi.size

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

properties = array([1660, 0, 1.99, 0.5, 0])

bottom_data = {"btype":btype, "ptype":ptype, "units":units,"itype":itype,"x":x,"y":y,"z":z,"properties":properties}

#==================================================================
#  
#  Define output data:
#  
#==================================================================

yarray = arange(0.035,4.95+0.005,0.005)*1000; nya = yarray.size
xarray = zeros( nya )
zarray =  ones( nya )*10

nxa = 0
nza = 0

miss = 0.5

output_data = {"ctype":"CPR","array_shape":"VRY","x":xarray,"y":yarray,"z":zarray,
               "nxa":nxa,"nya":nya,"nza":nza,"miss":miss}

print('Writing TRACEO3D waveguide input file...')

wtraceo3dinfil("lmacnrs.in",case_title,source_data,surface_data,ssp_data,bottom_data,output_data)

system('traceo3d.exe lmacnrs.in')

print('Reading the output data...')

data = loadmat('cpr.mat')

p  = squeeze( data["pressure"] )
p = where( p == 0, nan, p )
tl = 20*log10( abs( p ) )
yarray = squeeze( data["yarray3d"] )
rarraykm = yarray/1000

figure(1)
plot(rarraykm,tl)
xlabel('ACROSS SLOPE RANGE [in km]',fontsize=16)
ylabel('TLOSS [in dB]',fontsize=16)
grid(True)
show()

print('done.')
