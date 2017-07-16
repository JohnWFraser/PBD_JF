# This is a program which calculates 10 functions typically found on a calculator

import math

# math.radians in this next def/function converts degrees to radians
def sin(deg):
	return float(int(math.sin(math.radians(deg))*10**9+0.5))/10**9
	# (deals with rounding errors)

def reciprocal(x):
	if x==0:
		return ValueError
	else:
		return x**(-1)

def square(x):
	return x**2
	
def sqroot(x):
	if x<0:
		return ValueError
	else:
		return math.sqrt(x)

def cube(x):
	return x**3

def cuberoot(x):
	if x>=0:
		return x**(1.0/3)
	else:
		return (-x)**(1.0/3) *(-1)

def ypowerx(y,x):
	if y<0:
		if int(x) != x:
			# a negative number cannot be raised to a fractional power:
			return ValueError
		elif x<0:
			return (1.0/y)**(-x)
		else:
			return y**x
	else:
		return y**x

def ln(x):
	if x<0:
		return ValueError
	else:
		return math.log(x)

# log(x) to base 10:
def log10(x):
	if x<0:
		return ValueError
	else:
		return math.log(x)/math.log(10)
		# could have used math.log10(x) as "log10" is actually a recognised function in Python - but I did not realise this when first producing above, so leave as is

def	exp(x):
	return math.exp(x)


# sin(x): we will provide the sin of the numbers (angular degrees) provided
mylist_degrees = [0, 30, 45, 60, 90]
print "We want to get sin of each angle(given in degrees) in this list: ", mylist_degrees
output_sin = map(sin,mylist_degrees)
print "sine of each angle in above list is: ", output_sin
print

# reciprocal: we will provide 1/x for each of the numbers (x) provided
mylist_reciprocal = [0, 0.5, 4, 2, 8, -3]
print "We want to get the reciprocal of each number in this list: ", mylist_reciprocal
output_reciprocal = map(reciprocal,mylist_reciprocal)
print "reciprocal of each number in above list is: ", output_reciprocal
print

# square: we will provide square of each of the numbers (x) provided
mylist_square = [0, 0.5, 4, 2, 8, -3]
print "We want to get the square of each number in this list: ", mylist_reciprocal
output_square = map(square,mylist_square)
print "square of each number in above list is: ", output_square
print

# square root: we will provide square root of each of the numbers (x) provided
mylist_squareroot = [0, -2, 4, 0.25, 2, 81]
print "We want to get the square root of each number in this list: ", mylist_squareroot
output_squareroot = map(sqroot,mylist_squareroot)
print "square root of each number in above list is: ", output_squareroot
print

# cube: we will provide cube of each of the numbers (x) provided
mylist_cube = [0, 0.5, 2, -3, 8.5]
print "We want to get the cubee of each number in this list: ", mylist_cube
output_cube = map(cube,mylist_cube)
print "cube of each number in above list is: ", output_cube
print

# cube root: we will provide square root of each of the numbers (x) provided
mylist_cuberoot = [0, -2, 8, -27, 0.5]
print "We want to get the cube root of each number in this list: ", mylist_cuberoot
output_cuberoot = map(cuberoot,mylist_cuberoot)
print "cuberoot of each number in above list is: ", output_cuberoot
print

# generator comprehension
# y^x: we will provide y**x for each of the number couples (y, x) provided
max_s = 30
mylist_yprx = []
doublets = ((x,y) for x in range(1,max_s) for y in range(x,max_s)
	if 4*x+y == 50)
#print triplets
for value in doublets:
	#print value
	#print reduce(lambda x, y: x+y, value)
	mylist_yprx.append(value)
print "We want to provide y^x for each couple in this list: ", mylist_yprx
#output_yprx = map(ypowerx, mylist_yprx)
#print "y^x for each couple in above list is as follows: ", output_yprx
print

# ln (log base e): we will provide ln of each of the numbers (x) provided
mylist_ln_initial = [1, 10, 100, 2.718281828, -1.15]
# we want to strip out any numbers below 0 as ln(x) not defined for x<0 (could have sent through and allowed 'ValueError', but want to illustrate use of 'filter' 
mylist_ln = filter(lambda x: x>=0, mylist_ln_initial)
print "We want to get the (natural) ln of each number in this list: ", mylist_ln
output_ln = map(ln,mylist_ln)
print "ln of each number in above list is: ", output_ln
print

# generator comprehension
# we will generate a sequence of Pythagorean triplets
max_z = 30
mylist_log10 = []
triplets = ((x,y,z) for x in range(1,max_z) for y in range(x,max_z) for z in range(y, max_z)
	if x**2 + y**2 == z**2)
# we will now use the 'reduce' function to add the numbers in the triplets into one value and then append that value into a list:
for value in triplets:
	mylist_log10.append(reduce(lambda x, y: x+y, value))
print "We want to get log base 10 of each number in this list: ", mylist_log10
output = map(log10,mylist_log10)
print "log base 10 of each number in above list is: ", output
print

# exp: we will provide exp^x for each of the numbers (x) provided
mylist_exp = [0, 1, 5, -8.5, -1]
print "We want to get exp^x for each number in this list: ", mylist_exp
output_exp = map(exp,mylist_exp)
print "exp^x for each number in above list is: ", output_exp
print