def wtraceo3dinfil(filename=None, thetitle=None, source_info=None, surface_info=None, ssp_info=None, bathymetry_info=None, output_info=None):

    # Writes Traceo3D input (waveguide) file. 
    #
    # SYNTAX: wtraceo3dinfil( filename, title, source, surface, ssp, object, bottom, output )
    #

    #*******************************************************************************
    # Faro, Ter Jun 13 13:24:41 WEST 2017
    # Written by Orlando Camargo Rodriguez
    #*******************************************************************************
    
    separation_line = "--------------------------------------------------------------------------------"
    
    #*******************************************************************************
    # Get source data: 

    ds = source_info["ds"]
    xs = source_info["position"]
    xbox = source_info["xbox"]
    ybox = source_info["ybox"]
    freq = source_info["f"]
    thetas = source_info["thetas"]
    nthetas = source_info["nthetas"]
    phi     = source_info["phi"]
    nphi    = source_info["nphi"]

    theta1 = thetas[0]
    thetan = thetas[-1]
    
    phi1 = phi[0]
    phin = phi[-1]

    #*******************************************************************************
    # Get surface data: 

    atype = surface_info["btype"]
    aptype = surface_info["ptype"]
    aitype = surface_info["itype"]
    xati = surface_info["x"]
    yati = surface_info["y"]
    zati = surface_info["z"]
    atiu = surface_info["units"]
    aproperties = surface_info["properties"]
    
    nxati = xati.size
    nyati = yati.size    

    #*******************************************************************************
    # Get sound speed data: 

    ctype  = ssp_info["ctype"]

    c = ssp_info["c"]
    x = ssp_info["x"]
    y = ssp_info["y"]    
    z = ssp_info["z"]

    #*******************************************************************************  
    # Get bathymetry data:
    
    btype = bathymetry_info["btype"]
    bptype = bathymetry_info["ptype"]
    bitype = bathymetry_info["itype"]
    xbty = bathymetry_info["x"]
    ybty = bathymetry_info["y"]
    zbty = bathymetry_info["z"]
    btiu = bathymetry_info["units"]
    bproperties = bathymetry_info["properties"]
    
    nxbty = xbty.size
    nybty = ybty.size    

    #*******************************************************************************  
    # Get output options: 

    calc_type = output_info["ctype"]
    array_shape = output_info["array_shape"]
    xarray = output_info["x"]
    yarray = output_info["y"]
    zarray = output_info["z"]
    nxa    = output_info["nxa"]
    nya    = output_info["nya"]
    nza    = output_info["nza"]    
    array_miss = output_info["miss"]

    #*******************************************************************************  
    # Write the INFIL: 

    fid = open(filename, 'w')
    fid.write('\'');fid.write(thetitle);fid.write('\'\n')
    fid.write(separation_line);fid.write("\n")
    
    fid.write(str(ds))
    fid.write("\n")
    fid.write(str(xs[0]))
    fid.write(" ")
    fid.write(str(xs[1]))
    fid.write(" ")
    fid.write(str(xs[2]))
    fid.write("\n")   
    fid.write(str(freq))
    fid.write("\n")
    fid.write(str(xbox[0]))
    fid.write(" ")
    fid.write(str(xbox[1]))
    fid.write("\n")
    fid.write(str(ybox[0]))
    fid.write(" ")
    fid.write(str(ybox[1]))
    fid.write("\n")    
    fid.write(str(nthetas))
    fid.write("\n")
    if nthetas > 1:
       fid.write(str(theta1))
       fid.write(" ")
       fid.write(str(thetan))
    else:
       fid.write(str(theta1))     
    fid.write("\n")
    fid.write(str(nphi))
    fid.write("\n")
    if nphi > 1:
       fid.write(str(phi1))
       fid.write(" ")
       fid.write(str(phin))
    else:
       fid.write(str(phi1))
    fid.write("\n")    
    fid.write(separation_line);fid.write("\n")
    fid.write('\'');fid.write(atype) ;fid.write('\'\n')
    fid.write('\'');fid.write(aptype);fid.write('\'\n')
    fid.write('\'');fid.write(aitype);fid.write('\'\n')
    fid.write('\'');fid.write(atiu)  ;fid.write('\'\n')
    fid.write(str(nxati))
    fid.write("\n")
    for i in range(nxati):
        fid.write(str(xati[i]));fid.write(" ") 
    fid.write("\n")
    fid.write(str(nyati))
    fid.write("\n")
    for i in range(nyati):
        fid.write(str(yati[i]));fid.write(" ") 
    fid.write("\n")
    for j in range(nyati):
        for i in range(nxati):
            fid.write(str(zati[j,i]));fid.write(" ")
        fid.write("\n")
    if aptype == 'H':
       fid.write(str(aproperties[0]));fid.write(" ")
       fid.write(str(aproperties[1]));fid.write(" ")
       fid.write(str(aproperties[2]));fid.write(" ")
       fid.write(str(aproperties[3]));fid.write(" ")
       fid.write(str(aproperties[4]));fid.write('\n')
    elif aptype == 'N':
       for j in range(nyati):
           for i in range(nxati):
               fid.write(str(aproperties[0,j,i]));fid.write(" ")
           fid.write("\n")
       for j in range(nyati):
           for i in range(nxati):
               fid.write(str(aproperties[1,j,i]));fid.write(" ")
           fid.write("\n")
       for j in range(nyati):
           for i in range(nxati):
               fid.write(str(aproperties[2,j,i]));fid.write(" ")
           fid.write("\n")
       for j in range(nyati):
           for i in range(nxati):
               fid.write(str(aproperties[3,j,i]));fid.write(" ")
           fid.write("\n")
       for j in range(nyati):
           for i in range(nxati):
               fid.write(str(aproperties[4,j,i]));fid.write(" ")
           fid.write("\n")
    else:
       print('Unknown surface properties...')
    fid.write(separation_line);fid.write("\n")
    
# Analytical profiles: 
# Exponential   : 'EXPP'
# Inverse Square: 'ISQP'
# Isovelocity   : 'ISOV'
# Linear        : 'LINP'
# Munk          : 'MUNK'
# N2 Linear     : 'N2LP'
# Parabolic     : 'PARP'

# Tabulated:
# c(x,0,0)      : 'CX00'
# c(0,y,0)      : 'C0Y0'
# c(0,0,z)      : 'C00Z' 
# c(x,y,0)      : 'CXY0'
# c(x,0,z)      : 'CX0Z'
# c(0,y,z)      : 'C0YZ'
# c(x,y,z)      : 'CXYZ'

    fid.write('\'');fid.write(ctype);fid.write('\'\n')
    if  ( ctype == 'ISOV' ) or ( ctype == 'EXPP' ) or ( ctype == 'ISQP' ) or ( ctype == 'LINP' ) or \
        ( ctype == 'MUNK' ) or ( ctype == 'N2LP' ) or ( ctype == 'PARP' ):
       fid.write('2');fid.write('\n')
       fid.write(str(z[0]));fid.write(" ")
       fid.write(str(c[0]));fid.write("\n")
       fid.write(str(z[1]));fid.write(" ")
       fid.write(str(c[1]));fid.write("\n")
    elif ctype == 'C00Z':
       n = z.size
       fid.write(str(n));fid.write("\n")
       for i in range(n):
           fid.write(str(z[i]));fid.write(" ")
       fid.write("\n")
       for i in range(n):  
           fid.write(str(c[i]));fid.write(" ")
       fid.write("\n")
    elif ctype == 'CX00':
       n = x.size
       fid.write(str(n));fid.write("\n")
       for i in range(n):
           fid.write(str(x[i]));fid.write(" ")
       fid.write("\n")
       for i in range(n):  
           fid.write(str(c[i]));fid.write(" ")
       fid.write("\n")
    elif ctype == 'C0Y0':
       n = y.size
       fid.write(str(n));fid.write("\n")
       for i in range(n):
           fid.write(str(y[i]));fid.write(" ")
       fid.write("\n")
       for i in range(n):  
           fid.write(str(c[i]));fid.write(" ")
       fid.write("\n")
    elif ctype == 'CXY0':
       m = x.size
       n = y.size
       fid.write(str(m));fid.write(",") 
       fid.write(str(n));fid.write("\n")
       for i in range(m):
           fid.write(str(x[i]));fid.write(" ")
       fid.write("\n")
       for i in range(n):  
           fid.write(str(y[i]));fid.write(" ")
       fid.write("\n")
       for j in range(n):
           for i in range(m):
               fid.write(str(c[j,i]));fid.write(" ")
           fid.write("\n")
       fid.write("\n")
    elif ctype == 'CX0Z':
       m = x.size
       n = z.size
       fid.write(str(m));fid.write(",") 
       fid.write(str(n));fid.write("\n")
       for i in range(m):
           fid.write(str(x[i]));fid.write(" ")
       fid.write("\n")
       for i in range(n):  
           fid.write(str(z[i]));fid.write(" ")
       fid.write("\n")
       for j in range(n):
           for i in range(m):
               fid.write(str(c[j,i]));fid.write(" ")
           fid.write("\n")
       fid.write("\n")
    elif ctype == 'C0YZ':
       m = y.size
       n = z.size
       fid.write(str(m));fid.write(",") 
       fid.write(str(n));fid.write("\n")
       for i in range(m):
           fid.write(str(y[i]));fid.write(" ")
       fid.write("\n")
       for i in range(n):  
           fid.write(str(z[i]));fid.write(" ")
       fid.write("\n")
       for j in range(n):
           for i in range(m):
               fid.write(str(c[j,i]));fid.write(" ")
           fid.write("\n")
       fid.write("\n")
    elif ctype == 'CXYZ':
       nx = x.size
       ny = y.size
       nz = z.size
       fid.write(str(nx));fid.write(",")
       fid.write(str(ny));fid.write(",")
       fid.write(str(nz));fid.write("\n")
       for i in range(nx):
           fid.write(str(x[i]));fid.write(" ")
       fid.write("\n")
       for i in range(ny):  
           fid.write(str(y[i]));fid.write(" ")
       fid.write("\n")
       for i in range(nz):  
           fid.write(str(z[i]));fid.write(" ")
       fid.write("\n")  
       for ix in range(nz):
           for iy in range(ny):
               for ix in range(nx):
                   fid.write(str(c[iz,iy,ix]));fid.write(" ")
               fid.write("\n")
           fid.write("\n")
       fid.write("\n")
    else:
       print('Unknown sound speed distribution...')     
    fid.write(separation_line);fid.write("\n")
    fid.write("0\n")
    fid.write(separation_line);fid.write("\n")    
    fid.write('\'');fid.write(btype) ;fid.write('\'\n')
    fid.write('\'');fid.write(bptype);fid.write('\'\n')
    fid.write('\'');fid.write(bitype);fid.write('\'\n')
    fid.write('\'');fid.write(btiu)  ;fid.write('\'\n')
    fid.write(str(nxbty))
    fid.write("\n")
    for i in range(nxbty):
        fid.write(str(xbty[i]));fid.write(" ") 
    fid.write("\n")
    fid.write(str(nybty))
    fid.write("\n")
    for i in range(nybty):
        fid.write(str(ybty[i]));fid.write(" ") 
    fid.write("\n")
    for j in range(nybty):
        for i in range(nxbty):
            fid.write(str(zbty[j,i]));fid.write(" ")
        fid.write("\n")    
    if aptype == 'H':
       fid.write(str(bproperties[0]));fid.write(" ")
       fid.write(str(bproperties[1]));fid.write(" ")
       fid.write(str(bproperties[2]));fid.write(" ")
       fid.write(str(bproperties[3]));fid.write(" ")
       fid.write(str(bproperties[4]));fid.write('\n')
    elif aptype == 'N':
       for j in range(nybty):
           for i in range(nxbty):
               fid.write(str(bproperties[0,j,i]));fid.write(" ")
           fid.write("\n")
       for j in range(nybty):
           for i in range(nxbty):
               fid.write(str(bproperties[1,j,i]));fid.write(" ")
           fid.write("\n")
       for j in range(nybty):
           for i in range(nxbty):
               fid.write(str(bproperties[2,j,i]));fid.write(" ")
           fid.write("\n")
       for j in range(nybty):
           for i in range(nxbty):
               fid.write(str(bproperties[3,j,i]));fid.write(" ")
           fid.write("\n")
       for j in range(nybty):
           for i in range(nxbty):
               fid.write(str(bproperties[4,j,i]));fid.write(" ")
           fid.write("\n")
    else:
       print('Unknown bottom properties...')
    fid.write(separation_line);fid.write("\n")
    fid.write(str(nxa));fid.write(",")
    fid.write(str(nya));fid.write(",")
    fid.write(str(nza));fid.write("\n")
    if nxa*nya*nza == 0:
       nhyds = max([nxa,nya,nza])
       for i in range(nhyds):
          fid.write(str(xarray[i]));fid.write(" ")
          fid.write(str(yarray[i]));fid.write(" ")
          fid.write(str(zarray[i]));fid.write("\n")
    else:    	  
       for i in range(nxa):
           fid.write(str(xarray[i]));fid.write(" ")
       fid.write('\n')
       for i in range(nya):
           fid.write(str(yarray[i]));fid.write(" ")
       fid.write('\n')
       for i in range(nza):
           fid.write(str(zarray[i]));fid.write(" ")
       fid.write('\n')

    fid.write(separation_line);fid.write("\n")
    
    fid.write('\'');fid.write(calc_type);fid.write('\'\n')
    fid.write(str(array_miss));fid.write("\n")

    fid.close()
