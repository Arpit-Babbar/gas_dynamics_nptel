import numpy as np

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-M", type=float)
parser.add_argument("-gamma", type=float)
args = parser.parse_args()

assert None not in [args.M, args.gamma]

M = args.M
γ = args.gamma

P2_P1 = 1.0 + 2.0 * γ/(γ+1.0) * (M**2-1.0) 
rho2_rho1 = ( (γ+1.0) * M**2 )/(2.0 + (γ-1.0) * M**2)
u2_u1 = 1.0/rho2_rho1
T2_T1 = P2_P1 * u2_u1
P02_P01 = P2_P1**(-1.0/(γ-1.0)) * ( rho2_rho1 )**( γ/(γ-1.0) )

print("P2/P1 = 1.0 + 2.0 * γ/(γ+1.0) * (M**2-1.0) = ", P2_P1)
print("rho2/rho1 = ( (γ+1.0) * M**2 )/(2.0 + (γ-1.0) * M**2) = ", rho2_rho1)
print("u2/u1 = rho1/rho2 = ", u2_u1)
print("T2/T1 = (P2/P1) * (u2/u1) = ", T2_T1)
print("P02/P01 = (P2/P1)**(-1.0/(γ-1.0)) * ( rho2/rho1 )**( γ/(γ-1.0) ) = ", P02_P01) 

