
import math
from car import Car
from db import CarDB

# define some variables

ford = Car({'name': "mustang"})
ford.addFuel(0.5)
ford.start()
ford.drive(250.0)
print("ford=" + str(ford))

nissan = Car({'name':"rouge"})
nissan.fuel = 0.75

carDB = CarDB()
carDB.createCarTable()

carDB.save(nissan)
carDB.save(ford)
print(carDB.getCarIds())



