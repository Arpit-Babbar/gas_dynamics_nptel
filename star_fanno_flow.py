import numpy as np
from numpy import sqrt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-M', default = 'none', type = float)
parser.add_argument('-gamma', default = 'none', type = float)
args = parser.parse_args()

assert 'none' not in [args.M, args.gamma]
g = args.gamma
M = args.M

t_t_star = (g+1.0)/(2.0+(g-1.0)*(M**2))
p_p_star = (1.0/M) * sqrt( (g+1.0) / (2.0 + (g-1.0)*(M**2) ) )
rho_rho_star = (1.0/M) * sqrt( (2.0 + (g-1.0)*(M**2) ) / (g+1.0) )
p0_p0_star = (1.0/M) * ( (g+1.0) / (2.0 + (g-1.0)*(M**2) ) )**( (g+1.0)/(2.0*(g+1.0)) )
four_f_bar_l_star_d = (1.0 - M**2)/( g*(M**2) ) + (g+1.0)/(2.0*g) * np.log( ( (g+1.0) * (M**2) ) / ( 2.0 + (g-1.0) * (M**2) ) )

print("T/T* = ", t_t_star)
print("P/P* = ", p_p_star)
print("rho_/rho* = ", rho_rho_star)
print("p0/p0* = ", p0_p0_star)
print("4fL*/D = ", four_f_bar_l_star_d)
