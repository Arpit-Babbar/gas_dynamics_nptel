import numpy as np
import argparse
from scipy import optimize

parser = argparse.ArgumentParser()
parser.add_argument('-ratio', default = 'none', type = float)
parser.add_argument('-gamma', default = 'none', type = float)
parser.add_argument('-region', default = 'supersonic', type = str,
                    choices = ('subsonic', 'supersonic') )
args = parser.parse_args()

assert 'none' not in [args.ratio, args.gamma]
g = args.gamma
ratio = args.ratio

def mach(M):
    rhs  = ( 2.0 / (g+1.0) ) * ( 1.0 + 0.5*(g-1.0)*(M**2) )
    rhs  = rhs**( 0.5*( (g+1.0)/(g-1.0) )   )
    rhs *= 1.0/M
    return rhs - ratio

if args.region == 'subsonic':
    M = optimize.fsolve(mach,0.01)
else:
    M = optimize.fsolve(mach,1.2)

print("M = ",M)

