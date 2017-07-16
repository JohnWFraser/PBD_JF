import unittest		# From library
from CA4_calculator_JFraser import sin, reciprocal, square, sqroot, cube, cuberoot, ypowerx, ln, log10, exp

# test the functionality
class TestCalculator(unittest.TestCase):

# General comment - I rounded numbers where necessary below; I considered doing this for all, but it is not obvious that this would have saved any time

	def testSin(self):
		self.assertEqual([1,0,0.707106781,0.5,-0.999999999], map(sin,[90,0,45,30,-90]))
		
	def testReciprocal(self):
		self.assertEqual([ValueError, 2, 0.25, 0.5, 0.125], map(reciprocal,[0, 0.5,4,2,8]))
		self.assertEqual(-0.333333333, float(int(reciprocal(-3)*10**9-0.5))/10**9)
		
	def testSquare(self):
		self.assertEqual([0,0.25,4,9,72.25], map(square,[0,0.5,2,-3,8.5]))
		
	def testsqroot(self):
		self.assertEqual([ValueError,2,0.5,9], map(sqroot,[-2,4,0.25,81]))
		
	def testCube(self):
		# cube of a rational number always rational, so no need for rounding floating point issues
		self.assertEqual([0,0.125,8,-27,614.125], map(cube,[0,0.5,2,-3,8.5]))
		
	def testCubeRoot(self):
		self.assertEqual([0,2,-3], map(cuberoot,[0,8,-27]))
	
	def testYpowerx(self):
		self.assertEqual(1, ypowerx(0,0))
		self.assertEqual(0.707106781, float(int(ypowerx(0.5,0.5)*10**9+0.5))/10**9)
		self.assertEqual(ValueError, ypowerx(-0.5,0.5))
		self.assertEqual(ValueError, ypowerx(-15,0.5))
		self.assertEqual(-512, ypowerx(-2,9))
		self.assertEqual(-0.125, ypowerx(-2,-3))
		self.assertEqual(ValueError, ypowerx(-2,9.5))
		self.assertEqual(0.537284965, float(int(ypowerx(12,-0.25)*10**9-0.5))/10**9)

	def testln(self):
		self.assertEqual([0,ValueError], map(ln,[1,-1.5]))
		
	def testLogbase10(self):
		self.assertEqual([0.0,1.0,2.0], map(log10,[1,10,100]))

	def testExp(self):
		self.assertEqual(1, exp(0))

calculatorchoice = raw_input("Do you want to request a calculation (enter Y) or just allow program to test (enter anything other than Y)?")
if calculatorchoice == "Y":
	print "This is a program which calculates some basic functions found on a calculator"
	print "You will be asked to choose one of the following functions - enter the selection number and follow the instructions"
	print "NOTE: ONLY #2 OFFERS USER CHOICE TO ENTER A LIST OF NUMBERS - NO TIME TO FINISH? UNCLEAR IF NEEDED???!"
	print
	print "1 - sin x"
	print "2 - 1/x"
	print "3 - x^2"
	print "4 - square root"
	print "5 - x^3"
	print "6 - cube root"
	print "7 - y^x"
	print "8 - ln (natural log)"
	print "9 - log (base 10)"
	print "10 - exp(x)"
	print

	# User must now choose option from 1 to 10, next section ensures such a number is chosen (takes integer of number entered)
	selection = int(float(raw_input("Enter the function you wish to use (1-10): ")))
	#Ensure user chooses a number between 1 and 10 (numbers are rounded down to integers):
	invalid = 0
	mylist = []
	while invalid == 0:
		if selection <=10:
			if selection>0:
				invalid = 1
		if selection > 10:
			selection = int(float((raw_input("Invalid option - try again (1-10): "))))
			if selection <= 10:
				if selection > 0:
					invalid = 1
		if selection <0:
			selection = int(float(raw_input("Cannot be lower than 0, please enter again (1-10): ")))
			if selection > 0:
				if selection <=10:
					marker = 1

	if selection == 1:
		x = float(raw_input("Enter degrees: "))
		print "sin ", x, "deg = ",sin(x)

	if selection == 2:
		proceed = "y"
		while proceed == "y":
			x = raw_input("1/x - Enter x: ")
			if x == "":
				print "proceed now changing to n"
				proceed = "n"
			else:
				x = float(x)
				print "number entered: ", x
				print mylist
				mylist.append(x)
				print "this is mylist: ", mylist
		print "reciprocal of list is: ", map(reciprocal,mylist)

	if selection == 3:
		x = float(raw_input("x^2 - Enter x: "))
		print x, "^2 = ", square(x)

	if selection == 4:
		#invalid = 0
		x = float(raw_input("sq root(x) - Enter x: "))
		#while invalid == 0:
		#	if x<0:
		#		x = float(raw_input("Cannot be less than 0, Enter x again: "))
		#	else:
		#		invalid = 1
		print "sq root(",x,") = ", sqroot(x)

	if selection == 5:
		x = float(raw_input("x^3 - Enter x: "))
		print x, "^3 = ", cube(x)

	if selection == 6:
		x = float(raw_input("cube root (x) - Enter x: "))
		print x, "^(1/3) = ", cuberoot(x)

	if selection == 7:
		invalid = 0
		y = float(raw_input("y^x - Enter y: "))
		x = float(raw_input("y^x - Enter x: "))
		# next bit to deal with fact that a negative number cannot be raised to a fractional (non-integer) power:
		while invalid == 0:
			if y<0:
				if int(x) != x:
					print "try again, if y<0, then x cannot be fractional:"
					y = float(raw_input("y^x - Enter y: "))
					x = float(raw_input("y^x - Enter x: "))
				else:
					invalid = 1
			else:
				invalid = 1
		print y,"^",x," = ", ypowerx(y,x)

	if selection == 8:
		invalid = 0
		x = float(raw_input("log (base e)(x) - Enter x: "))
		while invalid == 0:
			if x<0:
				x = float(raw_input("Cannot be less than 0, Enter x again: "))
			else:
				invalid = 1
		print "log (base e)(",x,") = ", ln(x)

	if selection == 9:
		invalid = 0
		x = float(raw_input("log10(x) - Enter x: "))
		while invalid == 0:
			if x<0:
				x = float(raw_input("Cannot be less than 0, Enter x again: "))
			else:
				invalid = 1
		print "log (base 10)(",x,") = ", log10(x)

	if selection == 10:
		x = float(raw_input("(exp)^x - Enter x: "))
		print "e^",x," = ", exp(x)
		
if __name__ == '__main__':
	unittest.main()


