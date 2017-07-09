import unittest

from carR1_JFraser import Car, ElectricCar, DieselCar, HybridCar
from Rental2_JFraser import Dealership

# test the car functionality
class TestCar(unittest.TestCase):
    #dealership.create_current_stock(p, e ,d, h)
    def test_create_current_stock(self):
        self.carlist = Dealership()
        print "got this far"
        self.carlist.create_current_stock(20,4,8,8)
        print "got this far"
        print len(self.carlist.petrol_cars)
        #print self.carlist.petrol_cars
        #print self.carlist.diesel_cars
        print "6th car: ", self.carlist.petrol_cars[5]
        print "14th car: ", self.carlist.petrol_cars[13]
        self.carlist.rent(self.carlist.diesel_cars, self.carlist.diesel_rentlist, self.carlist.diesel_customerlist, 1, "J Kieran")
        self.carlist.rent(self.carlist.diesel_cars, self.carlist.diesel_rentlist, self.carlist.diesel_customerlist, 3, "J Fraser")
        self.carlist.rent(self.carlist.diesel_cars, self.carlist.diesel_rentlist, self.carlist.diesel_customerlist, 1, "T Daly")
        # In 3 lines above, we have rented out 5 (diesel) cars, 1st to J Kieran, 5th to T Daly and 2nd, 3rd, 4th to J Fraser
        #print self.carlist.diesel_cars
        print "cars currently rented out (diesel only): ", self.carlist.diesel_rentlist
        print "current customer list for above cars: ", self.carlist.diesel_customerlist
		
        self.assertEqual("J Kieran", self.carlist.diesel_customerlist[0])
        self.assertEqual("J Fraser", self.carlist.diesel_customerlist[3])
        self.carlist.returnn(self.carlist.diesel_cars, self.carlist.diesel_rentlist, self.carlist.diesel_customerlist, 2)
        #This returns 3rd car, so one of J Fraser entries removed, so T Daly should now be 4th record in customer list (with list reduced to 4)
        self.assertEqual("T Daly", self.carlist.diesel_customerlist[3])
        self.assertEqual(4, len(self.carlist.diesel_customerlist))
        print "just after asserting now.."

        self.carlist.rent(self.carlist.petrol_cars, self.carlist.petrol_rentlist, self.carlist.petrol_customerlist, 1, "J Kieran")
        self.carlist.rent(self.carlist.petrol_cars, self.carlist.petrol_rentlist, self.carlist.petrol_customerlist, 1, "F Hodges")
        self.carlist.rent(self.carlist.petrol_cars, self.carlist.petrol_rentlist, self.carlist.petrol_customerlist, 1, "J Bloggs")
        self.carlist.rent(self.carlist.petrol_cars, self.carlist.petrol_rentlist, self.carlist.petrol_customerlist, 1, "K Treacy")
        self.carlist.rent(self.carlist.petrol_cars, self.carlist.petrol_rentlist, self.carlist.petrol_customerlist, 4, "S O'Neill")
        self.carlist.rent(self.carlist.petrol_cars, self.carlist.petrol_rentlist, self.carlist.petrol_customerlist, 1, "P Kelly")
        self.carlist.rent(self.carlist.petrol_cars, self.carlist.petrol_rentlist, self.carlist.petrol_customerlist, 1, "G Clarke")
        self.carlist.rent(self.carlist.petrol_cars, self.carlist.petrol_rentlist, self.carlist.petrol_customerlist, 1, "J Neill")
        # In lines above, we have rented out 11 petrol cars, 1st to J Kieran, 2nd to F Hodges etc. (5th to 8th to S O'Neill)
        self.assertEqual("J Kieran", self.carlist.petrol_customerlist[0])
        self.assertEqual("J Bloggs", self.carlist.petrol_customerlist[2])
        self.assertEqual("S O'Neill", self.carlist.petrol_customerlist[6])
        self.assertEqual("P Kelly", self.carlist.petrol_customerlist[8])
        self.assertEqual("J Neill", self.carlist.petrol_customerlist[10])
        print "11th petrol car customer: ", self.carlist.petrol_customerlist[10]
        # JF note: when above tests run successfully, no message appears; changing anything, e.g. 1 letter in any of above, throws up an error. This shows tests are working!
        #print self.carlist.diesel_cars
        #print self.carlist.diesel_rentlist

        self.carlist.returnn(self.carlist.petrol_cars, self.carlist.petrol_rentlist, self.carlist.petrol_customerlist, 9)
        #This returns 9th car, so P Kelly entry removed, so G Clarke should now be 9th record in customer list (with list reduced from 11 to 10)
        self.assertEqual("G Clarke", self.carlist.petrol_customerlist[8])
        self.assertEqual(10, len(self.carlist.petrol_customerlist))

        self.carlist.rent(self.carlist.electric_cars, self.carlist.electric_rentlist, self.carlist.electric_customerlist, 1, "F Shaw")
        self.carlist.rent(self.carlist.electric_cars, self.carlist.electric_rentlist, self.carlist.electric_customerlist, 1, "K Connor")
        self.carlist.rent(self.carlist.electric_cars, self.carlist.electric_rentlist, self.carlist.electric_customerlist, 1, "M Higgins")
        self.carlist.returnn(self.carlist.electric_cars, self.carlist.electric_rentlist, self.carlist.electric_customerlist, 1)
        #This returns 1st car, so F Shaw entry removed and M Higgins should now be 2nd and final record in customer list
        self.assertEqual("M Higgins", self.carlist.electric_customerlist[1])
        self.assertEqual(2, len(self.carlist.electric_customerlist))

        self.carlist.rent(self.carlist.hybrid_cars, self.carlist.hybrid_rentlist, self.carlist.hybrid_customerlist, 1, "J Bloggs3")
        self.carlist.rent(self.carlist.hybrid_cars, self.carlist.hybrid_rentlist, self.carlist.hybrid_customerlist, 1, "T Reilly")
        self.carlist.rent(self.carlist.hybrid_cars, self.carlist.hybrid_rentlist, self.carlist.hybrid_customerlist, 1, "L Coghlan")
        self.carlist.returnn(self.carlist.hybrid_cars, self.carlist.hybrid_rentlist, self.carlist.hybrid_customerlist, 2)
        print "Hybrid customer list after 1 returned", self.carlist.hybrid_customerlist
        #This returns 2nd car, so T Reilly entry removed and L Coghlan should now be 2nd and final record in customer list
        self.assertEqual("L Coghlan", self.carlist.hybrid_customerlist[1])
        self.assertEqual(2, len(self.carlist.hybrid_customerlist))
        self.carlist.returnn(self.carlist.hybrid_cars, self.carlist.hybrid_rentlist, self.carlist.hybrid_customerlist, 1)
        #This returns 1st car, so J Bloggs3 entry removed and L Coghlan should now be the 1 and only record in customer list
        self.assertEqual("L Coghlan", self.carlist.hybrid_customerlist[0])
        self.assertEqual(1, len(self.carlist.hybrid_customerlist))		

    #def test_rent(self):
        #self.carlist = Dealership()
        #print "got this far"
        #self.carlist.rent(self.carlist.diesel_cars, self.carlist.diesel_rentlist, self.carlist.diesel_customerlist, 1, "J Fraser")
        #print self.carlist.diesel_cars
        #print self.carlist.diesel_rentlist
        #print self.carlist.diesel_customerlist
        #print "got this far again!"
        #print len(self.carlist.petrol_cars)
        #print self.carlist.diesel_rentlist[0]
        #print self.carlist.diesel_customerlist[0]
        #print self.carlist.petrol_cars[13]
		
    #def newtest(self):
        #ff = self.carlist.create_current_stock(10,20,10)
        #print "got this far", ff#self.assertEqual(10, self.carlist.len(diesel_cars))
        #self.assertEqual(40, car_fleet.getNumAvailable())


        #car_fleet.rentCar(5)
        #self.assertEqual(100, car_fleet.getProfit())
        #self.assertEqual(35, car_fleet.getNumAvailable())


        #car_fleet.returnCar(2)
        #self.assertEqual(37, car_fleet.getNumAvailable())


        #car_fleet.returnCar(3)
        #self.assertEqual(40, car_fleet.getNumAvailable())

        #car_fleet.returnCar(3)
        #car_fleet.rentCar(50)

if __name__ == '__main__':
    unittest.main()
