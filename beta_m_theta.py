import numpy as np
from numpy import sin, cos, tan
from scipy import optimize
import argparse

# Get arguments

parser = argparse.ArgumentParser()
parser.add_argument('-M', default = 'none', type = float)
parser.add_argument('-theta', default = 'none', type = float)
parser.add_argument('-gamma', default = 'none', type = float)
args = parser.parse_args()

assert 'none' not in [args.M, args.theta, args.gamma]
theta = args.theta
g     = args.gamma
M     = args.M
tan_theta = tan(theta)

def t(beta):
  cot_beta = 1.0 / np.tan(beta)
  return 2.0 * cot_beta * ( (M**2 * sin(beta)**2 - 1) / (M**2 * (g + cos(2.0*beta)) + 2.0 ) ) - tan_theta

beta = optimize.fsolve(t, 0.1)

print("In radians, beta = ", beta, ", in degree, beta = ", beta * 180 / np.pi)

