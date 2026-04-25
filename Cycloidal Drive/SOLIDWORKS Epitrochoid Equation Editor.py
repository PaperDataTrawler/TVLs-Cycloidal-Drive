import math
R = 1.375
r = 0.15748
N = 21
E = 0.03125

print(f"FOR X: ({R}*cos(t))-({r}*cos(t+arctan(sin((1-{N})*t)/(({R}/({E}*{N}))-cos((1-{N})*t)))))-({E}*cos({N}*t))")
print(f"FOR Y: (-{R}*sin(t))+({r}*sin(t+arctan(sin((1-{N})*t)/(({R}/({E}*{N}))-cos((1-{N})*t)))))+({E}*sin({N}*t))")
print("FOR T1: ((-10/360)*(2*pi))")
print("FOR T2: (190/360)*(2*pi)")