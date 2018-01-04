# Problem: You code for interacting with the latest web authentication scheme has encountered a
# singularity and your only solution is to go around it in the complex plane. Or maybe you just
# need to perform some calculations using complex numbers.

a = complex(2, 4)
b = 3 - 5j
a # (2+4j)
b # (3-5j)

a.real # 2.0
a.img # 4.0
a.conjugate() # (2-4j)

# In addition, all of the usual mathematical operators work:
a + b # (5-1j)
a * b # (26+2j)

# To perform additional complex-valued functions such as sines, cosines, or square roots, use
# the cmath module
import cmath
cmath.sin(a) # (24.83130584894638-11.356612711218174j)
cmath.cos(a) # (-11.36423470640106-24.814651485634187j)
cmath.exp(a) # (-4.829809383269385-5.5920560936409816j)

# discussion
# if you want complex numbers to be produced as a result, you have to explicitly use cmath or
# declare the use of a complex type in libraries that know about them
import cmath
cmath.sqrt(-1)
