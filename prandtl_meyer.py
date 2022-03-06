import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-M', default = 'none', type = float)
parser.add_argument('-gamma', default = 'none', type = float)
args = parser.parse_args()

assert 'none' not in [args.M, args.gamma]
g = args.gamma
M = args.M

nu  = np.sqrt( (g+1.0)/(g-1.0) ) * np.arctan( np.sqrt((g-1)/(g+1) * (M**2-1) ) ) - np.arctan( np.sqrt(M**2-1.0))

print("nu in radians ", nu, "mu in degrees = ", nu * 180/np.pi)

