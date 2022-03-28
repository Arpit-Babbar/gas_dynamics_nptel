import numpy as np
import argparse
from scipy import optimize

parser = argparse.ArgumentParser()
parser.add_argument("-p0_p", type=float)
parser.add_argument("-gamma", type=float)
args = parser.parse_args()

assert None not in [args.p0_p, args.gamma]

p0_p = args.p0_p
γ = args.gamma

def mach(M):
    rhs = (1 + 0.5*(γ-1.0) * M**2 )
    rhs = rhs**(γ/(γ-1.0))
    return rhs-p0_p

M = optimize.fsolve(mach, 10.0)

print("M = ", M)


