import numpy as np
import argparse

# Get arguments

parser = argparse.ArgumentParser()
parser.add_argument('-M', default = 'none', type = float)
parser.add_argument('-beta', default = 'none', type = float)
parser.add_argument('-gamma', default = 'none', type = float)
args = parser.parse_args()

assert 'none' not in [args.M, args.beta, args.gamma]
b = args.beta
g = args.gamma
M = args.M

cot_beta = 1.0 / np.tan(b)

tan_theta = 2.0 * cot_beta * ( (M**2 * np.sin(b)**2 - 1) / (M**2 * (g + np.cos(2.0*b)) + 2.0 ) )

print("tan_theta = ", tan_theta)

theta = np.arctan(tan_theta)
print("In radians, theta = ", theta, ", in degree, theta = ", theta * 180 / np.pi)

