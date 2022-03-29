import numpy as np
from numpy import log
from scipy import optimize
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-friction', default = 'none', type = float)
parser.add_argument('-gamma', default = 'none', type = float)
parser.add_argument('-region', default = 'supersonic', type = str,
                    choices = ('subsonic', 'supersonic') )
args = parser.parse_args()

assert 'none' not in [args.friction, args.gamma]
g = args.gamma
fric = args.friction

def mach(M):
    rhs = fric - ( (1.0-M**2)/(g*M**2) + (g+1.0)/(2.0*g) * log( ( (g+1.0)*M**2 )/(2.0+(g-1.0)*(M**2) ) ) )
    return rhs

if args.region == 'subsonic':
    M = optimize.fsolve(mach,0.01)
else:
    M = optimize.fsolve(mach,1.2)


print("M = ",M)

