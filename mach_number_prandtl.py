import numpy as np
from numpy import sin, cos, tan, sqrt
from scipy import optimize
import argparse

# Get arguments

parser = argparse.ArgumentParser()
parser.add_argument('-M', default = 'none', type = float)
parser.add_argument('-gamma', default = 'none', type = float)
args = parser.parse_args()

assert 'none' not in [args.M, args.gamma]
g     = args.gamma
M     = args.M

m2_sqr =  (1 + (g-1.0)/2.0 * M**2 ) / (g*M**2 - (g-1.0)/2.0 )
m2 = sqrt(m2_sqr)
print("M2 = ", m2)
