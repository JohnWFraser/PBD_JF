# this was started by taking June14_car.py and removing all coding below the "def"s
# We are introducing a sub-class (electric Car) at bottom


class Car:

	def __init__(self):
		self.__make = 'Ferrari'
		self.__colour = 'Red'
		self.__mileage = 10
		self.engineSize = '5.4l'

	def getMake(self):
		return self.__make

	def getColour(self):
		return self.__colour

	def getMileage(self):
		return self.__mileage
	
	def setMake(self, make):
		self.__make = make
	
	def setColour(self, colour):
		self.__colour = colour
	
	def setMileage(self, mileage):
		self.__mileage = mileage
	
	def move3(self, distance):
		self.__mileage = self.__mileage + distance
	
	def paint(self, colour):
		print('Getting a paint job - new colour is: ' + colour)
		self.__colour = colour

class electricCar(Car):

	def __init__(self):
		Car.__init__(self)
		self.__numberFuelCells = 2
	
	def getNumberFuelCells(self):
		return self.__numberFuelCells
	
	def setNumberFuelCells(self, value):
		self.__numberFuelCells = value


