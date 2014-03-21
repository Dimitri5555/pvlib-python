# Autogenerated with SMOP version 0.23
# /usr/local/bin/smop pvl_grounddiffuse.m -o python/pvl_grounddiffuse.py
import numpy as np
import pvl_tools 

def pvl_grounddiffuse(**kwargs):
    Expect={'DataFrame':'df',
            'SurfTilt':('num'),
            'GHI':('matelement','num','array','x>=0'),
            'Albedo':('num','array','x>=0','x<=1'),
            }

    var=pvl_tools.Parse(kwargs,Expect)

    GR=var.DataFrame.GHI*(var.Albedo)*((1 - np.cos(np.radians(var.SurfTilt)))*(0.5))

    var.DataFrame['GR']=GR
    
    return var.DataFrame