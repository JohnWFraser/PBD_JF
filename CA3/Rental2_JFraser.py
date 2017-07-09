
from carR1_JFraser import Car, ElectricCar, PetrolCar, DieselCar, HybridCar

class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []
        self.electric_rentlist = []
        self.electric_customerlist = []
        self.petrol_rentlist = []
        self.petrol_customerlist = []
        self.diesel_rentlist = []
        self.diesel_customerlist = []
        self.hybrid_rentlist = []
        self.hybrid_customerlist = []
		
    def create_current_stock(self, p, e, d, h):
        for i in range(e):
           self.electric_cars.append(ElectricCar())
        for i in range(p):
           self.petrol_cars.append(PetrolCar())
        for i in range(d):
           self.diesel_cars.append(DieselCar())
        for i in range(h):
           self.hybrid_cars.append(HybridCar())
           #return 45

    def stock_count(self):
        print 'petrol cars in stock ' + str(len(self.petrol_cars))
        print 'electric cars in stock ' + str(len(self.electric_cars))
        print 'diesel cars in stock ' + str(len(self.diesel_cars))
        print 'hybrid cars in stock ' + str(len(self.hybrid_cars))

    def rent(self, car_list, rent_list, cust_list, amount, name):
#       print car_list
#        print rent_list		
        if len(car_list) < amount:
            print 'Not enough cars in stock'
            return
        total = 0
		
        while total < amount:
           rent_list.append(car_list.pop(0)) #this actually reads the first element of car_list into rent_list, then deletes it from car_list!!
           cust_list.append(name)
		   #           car_list.pop(0)
           total = total + 1

    def process_rental(self):
        answer = 'y'
        # above line now superfluous, but easier to set at y than delete and change indentations below... raw_input('would you like to rent a car? y/n')
        if answer == 'y':
            answer = raw_input('what type (petrol, electric, diesel or hybrid) would you like?  - enter p/e/d/h: ')
            amount = int(raw_input('how many would you like to rent?'))
            name = raw_input('Please enter your name: ')
            if answer == 'p':
				self.rent(self.petrol_cars, self.petrol_rentlist, self.petrol_customerlist, amount, name)
            elif answer == 'e':
				self.rent(self.electric_cars, self.electric_rentlist, self.electric_customerlist, amount, name)
            elif answer == 'h':
				self.rent(self.hybrid_cars, self.hybrid_rentlist, self.hybrid_customerlist, amount, name)
            else:
				self.rent(self.diesel_cars, self.diesel_rentlist, self.diesel_customerlist, amount, name)
				#print self.diesel_cars
				x = len(self.diesel_rentlist)
				print "cars now assigned to you: ", self.diesel_rentlist[x-amount:]# just showing the car(s) assigned to latest customer only
				#print self.diesel_customerlist
        self.stock_count()

    def returnn(self, car_list, rent_list, cust_list, testmarker):
        amt = len(rent_list)
        total = 0
        if testmarker > 0:
		    number = testmarker-1# remember that this only applies when testing
        if testmarker == 0:
		    while total < amt:
		        print total,": ", rent_list[total]
		        total = total + 1
		    number = int(raw_input('enter number above which you want to return: '))
        car_list.append(rent_list.pop(number))
        cust_list.pop(number)

    def process_return(self):
        testmarker = 0 # this will allow function returnn to differentiate between testsuite run and actual run
        answer = raw_input('what type ((petrol, electric, diesel or hybrid) are you returning? p/e/d/h: ')
        if answer == 'p':
            self.returnn(self.petrol_cars, self.petrol_rentlist, self.petrol_customerlist, testmarker)
        elif answer == 'e':
            self.returnn(self.electric_cars, self.electric_rentlist, self.electric_customerlist, testmarker)
        elif answer == 'h':
            self.returnn(self.hybrid_cars, self.hybrid_rentlist, self.hybrid_customerlist, testmarker)
        else:
			print "assumed diesel car being returned"# doesn't actually check that d was entered, hence this comment
			self.returnn(self.diesel_cars, self.diesel_rentlist, self.diesel_customerlist, testmarker)
			print "cars in stock: ", self.diesel_cars
			print "cars now rented out: ", self.diesel_rentlist
			print "customer list for above: ", self.diesel_customerlist
			# above 3 lines would only be printed if app meant foruse by a company operator - would be delted otherwise; I include as may help for examination/marking purposes!
        self.stock_count()
		
		
dealership = Dealership()
p = 20
e = 4
d = 8
h = 8
dealership.create_current_stock(p, e , d, h)
# added July4:
dealership.stock_count()
#end July4

proceed1 = raw_input("if you wish to use this app to rent or return a car, please enter y now; for running tests only please enter n: ")

if proceed1 == 'y':
	proceed = 'y'
else:
	proceed = 'n'

# cnnot get below lines working - out if time! (11.35pm, 09/07/2017!!)
#print self.petrol_cars[2]
#totalstock = 0#int(len(self.petrol_cars))#+len(self.diesel_cars)+len(self.electric_cars)+len(self.hybrid_cars)
#if totalstock == 0:
#	proceed = 'n'
#	print ("Sorry, nothing to rent, please try again later")

while proceed == 'y':
    rent = raw_input('Do you wish to rent a car? y/n')
    if rent == 'y':
		dealership.process_rental()
    else:
        returnn = raw_input('Do you wish to return a car? y/n')
        if returnn == 'y':
			dealership.process_return()
    proceed = raw_input('continue? y/n')

