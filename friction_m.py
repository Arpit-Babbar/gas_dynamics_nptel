import numpy as np
from numpy import log
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-M', default = 'none', type = float)
parser.add_argument('-gamma', default = 'none', type = float)
args = parser.parse_args()

assert 'none' not in [args.M, args.gamma]
g = args.gamma
M = args.M

fric = (1.0-M**2)/(g*M**2) + (g+1.0)/(2.0*g) * log( ( (g+1.0)*M**2 )/(2.0+(g-1.0)*(M**2) ) )

print("4fL*/D = ",fric)

