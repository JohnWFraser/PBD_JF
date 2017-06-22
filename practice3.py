#input1 = float(raw_input("Enter first number: "))
#input2 = float(raw_input("Enter second number: "))

#print input1/input2
#output3 = input1 / input2

#print "first divided by second is: ", output3

import math

input1 = float(raw_input("Enter first angle in degrees: "))
y = math.radians(input1)		# converts degrees to radians
x = math.sin(y)
print "sine of ", input1, "is: ",x


#input1 = float(raw_input("Enter number of which square root to be calculated: "))

# x = math.sqrt(input1)
#print "square root of ", input1, "is: ",x
# JF: also, add if statement (like for divide function) to deal with x<0

#input1 = float(raw_input("Enter number to be cubed: "))
#x = input1**3
#print "the cube of ", input1, "is: ",x

#input1 = float(raw_input("Enter number for which natural log (base e) to be calculated: "))
#x = math.log(input1)
#print "the natural log of ", input1, "is: ",x

#input1 = float(raw_input("Enter number for which reciprocal is to be calculated: "))
#x = 1/input1
#print "the reciprocal of ", input1, "is: ",x

#input1 = float(raw_input("Enter number for which cube root is to be calculated: "))
#if input1>=0:
#	x = input1**(1.0/3)
#else:
#	x = (-input1)**(1.0/3) *(-1)
#print "the cube root of ", input1, "is: ",x

#input1 = float(raw_input("Enter number to be raised to a requested power: "))
#input2 = float(raw_input("Enter power to which first number is to be raised: "))
#if input1>=0:
#	x = input1**input2
#else:
#	x = (-input1)**input2 * (-1)
#	print " ", input1," to the power of ", input2, "is: ",x
