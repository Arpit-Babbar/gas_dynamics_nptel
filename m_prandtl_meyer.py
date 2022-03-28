import numpy as np
import argparse
from scipy import optimize

parser = argparse.ArgumentParser()
parser.add_argument('-nu', default = 'none', type = float)
parser.add_argument('-gamma', default = 'none', type = float)
args = parser.parse_args()

assert 'none' not in [args.nu, args.gamma]
g = args.gamma
nu = args.nu

print("Ensure that nu is in radians!")

def mach(M):
  return -(np.sqrt( (g+1.0)/(g-1.0) ) * np.arctan( np.sqrt((g-1)/(g+1) * (M**2-1) ) ) - np.arctan( np.sqrt(M**2-1.0)))+nu

M = optimize.fsolve(mach,1.1)

print("M = ", M)

