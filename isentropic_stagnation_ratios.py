import numpy as np

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-M", type=float)
parser.add_argument("-gamma", type=float)
args = parser.parse_args()

assert None not in [args.M, args.gamma]

M = args.M
γ = args.gamma

T0_T = (1 + 0.5*(γ-1.0) * M**2 )
P0_P = T0_T**(γ/(γ-1.0))
rho0_rho = T0_T**(1.0/(γ-1.0))

print("T0/T = (1 + 0.5*(γ-1.0) * M^2 ) = ",T0_T)
print("P0/P = (1 + 0.5*(γ-1.0) * M^2 )^(γ/(γ-1)) = ",P0_P)
print("ρ0/ρ = (1 + 0.5*(γ-1.0) * M^2 )^(1/(γ-1)) = ",rho0_rho)

