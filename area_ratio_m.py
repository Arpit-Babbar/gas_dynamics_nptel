import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-M', default = 'none', type = float)
parser.add_argument('-gamma', default = 'none', type = float)
args = parser.parse_args()

assert 'none' not in [args.M, args.gamma]
g = args.gamma
M = args.M

ratio  = ( 2.0 / (g+1.0) ) * ( 1.0 + 0.5*(g-1.0)*(M**2) )
ratio  = ratio**( 0.5*( (g+1.0)/(g-1.0) )   )
ratio *= 1.0/M

print("A/A* =",ratio)

