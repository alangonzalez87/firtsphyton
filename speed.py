import math
import time
import sys

# m = mass
# e_g = earth gravity
# j_g = jupiter gravity
# t = time in seconds
# C = 1/2 p A C
# exp = exponent
# sqrt = square root

print('Welcome to the velocity calculator. Please enter the following:\n')

m = float(input('Mass (in kg):'))
g = float(input('Gravity ( in m/s^2, 9.8 for Earth, 24 for Jupiter):'))
t = float(input ('Time (in seconds):'))
p = float(input ('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water):'))
A = float(input('Cross sectional area (in m^2):'))
C = float(input('Drag constant(0.5 for shere, 1.1 for cylinder):'))
print()

# First calculate = C = 1/2 p A C
c = ( 1 / 2 ) * p * A * C

print()

# Now calculate the velocity v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)*t))

v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

print()
print(f'(The inner value of c is: {c:.3f}')
print(f'The velocity after {t} second is: {v:.3f} m/s')
print()
print()

